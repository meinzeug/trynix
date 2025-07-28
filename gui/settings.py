from __future__ import annotations

from PySide6 import QtWidgets

from services.openrouter import load_api_key, save_api_key
from core.config import CONFIG, CONFIG_PATH


class SettingsWindow(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Settings")

        self.key_edit = QtWidgets.QLineEdit()
        try:
            self.key_edit.setText(load_api_key())
        except Exception:
            pass
        self.tts_check = QtWidgets.QCheckBox("Enable Queen TTS")
        self.tts_check.setChecked(CONFIG.tts_enabled)
        save_btn = QtWidgets.QPushButton("Save")

        layout = QtWidgets.QFormLayout(self)
        layout.addRow("OpenRouter API Key", self.key_edit)
        layout.addRow(self.tts_check)
        layout.addWidget(save_btn)

        save_btn.clicked.connect(self.save)

    def save(self) -> None:
        save_api_key(self.key_edit.text())
        CONFIG.tts_enabled = self.tts_check.isChecked()
        CONFIG.save(CONFIG_PATH)
        QtWidgets.QMessageBox.information(self, "Settings", "Saved")
        self.accept()
