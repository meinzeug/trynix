from __future__ import annotations

from PySide6 import QtWidgets
from core.agent_store import add_agent


class AgentCreatorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Create Agent")

        self.name_edit = QtWidgets.QLineEdit()
        self.desc_edit = QtWidgets.QLineEdit()
        self.spec_edit = QtWidgets.QLineEdit()
        self.abilities_edit = QtWidgets.QLineEdit()

        form = QtWidgets.QFormLayout(self)
        form.addRow("Name", self.name_edit)
        form.addRow("Beschreibung", self.desc_edit)
        form.addRow("Spezialisierung", self.spec_edit)
        form.addRow("F\xc3\xa4higkeiten", self.abilities_edit)

        save_btn = QtWidgets.QPushButton("Save")
        form.addWidget(save_btn)
        save_btn.clicked.connect(self.save)

    def save(self) -> None:
        name = self.name_edit.text().strip()
        if not name:
            QtWidgets.QMessageBox.warning(self, "Input", "Name required")
            return
        agent = {
            "name": name,
            "description": self.desc_edit.text().strip(),
            "specialization": self.spec_edit.text().strip(),
            "abilities": self.abilities_edit.text().strip(),
        }
        try:
            add_agent(agent)
        except ValueError as exc:
            QtWidgets.QMessageBox.warning(self, "Agent", str(exc))
            return
        QtWidgets.QMessageBox.information(self, "Agent", "Saved")
        self.accept()
