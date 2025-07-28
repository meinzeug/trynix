from __future__ import annotations

from PySide6 import QtWidgets

from db import add_message, get_messages, get_project
from core.roadmap import save_roadmap
from pathlib import Path
import json

from speech import transcribe_from_microphone, speak
from core.config import CONFIG

class ChatWindow(QtWidgets.QWidget):
    def __init__(self, conn, project_id: int) -> None:
        super().__init__()
        self.conn = conn
        self.project_id = project_id
        self.setWindowTitle("Chat")

        self.messages_view = QtWidgets.QTextEdit(readOnly=True)
        self.input_edit = QtWidgets.QLineEdit()
        self.send_btn = QtWidgets.QPushButton("Send")
        self.mic_btn = QtWidgets.QPushButton("🎤")
        self.tts_btn = QtWidgets.QPushButton("🔈")
        self.roadmap_btn = QtWidgets.QPushButton("Add to Roadmap")

        input_layout = QtWidgets.QHBoxLayout()
        input_layout.addWidget(self.input_edit)
        input_layout.addWidget(self.mic_btn)
        input_layout.addWidget(self.tts_btn)
        input_layout.addWidget(self.send_btn)
        input_layout.addWidget(self.roadmap_btn)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.messages_view)
        layout.addLayout(input_layout)

        self.send_btn.clicked.connect(self.send_message)
        self.mic_btn.clicked.connect(self.fill_from_speech)
        self.tts_btn.clicked.connect(self.speak_last)
        self.roadmap_btn.clicked.connect(self.add_to_roadmap)
        self.load_messages()

    def load_messages(self) -> None:
        self.messages_view.clear()
        for row in get_messages(self.conn, self.project_id):
            self.messages_view.append(f"{row['timestamp']} {row['sender']}: {row['message']}")

    def send_message(self) -> None:
        text = self.input_edit.text().strip()
        if text:
            add_message(self.conn, self.project_id, "user", text)
            self.input_edit.clear()
            self.load_messages()
    def fill_from_speech(self) -> None:
        try:
            text = transcribe_from_microphone()
            if text:
                self.input_edit.setText(text)
        except Exception as exc:
            QtWidgets.QMessageBox.warning(self, "STT Error", str(exc))

    def speak_last(self) -> None:
        text = self.input_edit.text().strip()
        if not text:
            text = self.messages_view.toPlainText().splitlines()[-1] if self.messages_view.toPlainText() else ""
        if text and CONFIG.tts_enabled:
            speak(text)

    def add_to_roadmap(self) -> None:
        text = self.input_edit.text().strip()
        if not text:
            return
        try:
            row = get_project(self.conn, self.project_id)
            if row and row["roadmap"]:
                path = Path(row["roadmap"])
                data = json.loads(path.read_text(encoding="utf-8"))
                if data.get("milestones"):
                    data["milestones"][0].setdefault("tasks", []).append({"title": text, "status": "open"})
                save_roadmap(data, path)
                add_message(self.conn, self.project_id, "queen", f"Roadmap updated with: {text}")
                self.input_edit.clear()
                self.load_messages()
        except Exception as exc:
            QtWidgets.QMessageBox.warning(self, "Roadmap", str(exc))


