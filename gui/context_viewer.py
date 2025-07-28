from __future__ import annotations

from pathlib import Path
from PySide6 import QtWidgets, QtCore


class ContextWindow(QtWidgets.QWidget):
    """Simple viewer for the global context state."""

    def __init__(self, path: Path) -> None:
        super().__init__()
        self.path = path
        self.setWindowTitle("Context State")

        self.text = QtWidgets.QPlainTextEdit(readOnly=True)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.text)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.load)
        self.timer.start(1000)
        self.load()

    def load(self) -> None:  # pragma: no cover - file IO
        if self.path.exists():
            try:
                self.text.setPlainText(self.path.read_text(encoding="utf-8"))
            except Exception:
                self.text.setPlainText("")
        else:
            self.text.setPlainText("<no context>")
