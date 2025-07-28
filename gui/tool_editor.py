from __future__ import annotations

from PySide6 import QtWidgets

from core.tool_store import add_tool


class ToolEditorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Create Tool")

        self.name_edit = QtWidgets.QLineEdit()
        self.desc_edit = QtWidgets.QLineEdit()
        self.cmd_edit = QtWidgets.QLineEdit()
        self.params_edit = QtWidgets.QLineEdit()

        form = QtWidgets.QFormLayout(self)
        form.addRow("Name", self.name_edit)
        form.addRow("Beschreibung", self.desc_edit)
        form.addRow("Kommando", self.cmd_edit)
        form.addRow("Parameter", self.params_edit)

        save_btn = QtWidgets.QPushButton("Save")
        form.addWidget(save_btn)
        save_btn.clicked.connect(self.save)

    def save(self) -> None:
        name = self.name_edit.text().strip()
        if not name:
            QtWidgets.QMessageBox.warning(self, "Input", "Name required")
            return
        tool = {
            "name": name,
            "description": self.desc_edit.text().strip(),
            "command": self.cmd_edit.text().strip(),
            "params": self.params_edit.text().strip(),
        }
        try:
            add_tool(tool)
        except ValueError as exc:
            QtWidgets.QMessageBox.warning(self, "Tool", str(exc))
            return
        QtWidgets.QMessageBox.information(self, "Tool", "Saved")
        self.accept()
