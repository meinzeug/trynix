from __future__ import annotations

from PySide6 import QtWidgets

from services.openrouter import load_api_key, save_api_key


class SettingsWindow(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Settings")

        self.key_edit = QtWidgets.QLineEdit()
        try:
            self.key_edit.setText(load_api_key())
        except Exception:
            pass
        save_btn = QtWidgets.QPushButton("Save")

        layout = QtWidgets.QFormLayout(self)
        layout.addRow("OpenRouter API Key", self.key_edit)
        layout.addWidget(save_btn)

        save_btn.clicked.connect(self.save)

    def save(self) -> None:
        save_api_key(self.key_edit.text())
        QtWidgets.QMessageBox.information(self, "Settings", "Saved")
        self.accept()
