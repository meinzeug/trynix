from __future__ import annotations

from PySide6 import QtWidgets, QtCore

from core.agents import AGENT_REGISTRY, AGENT_ACTIVE, activate_agent, deactivate_agent


class AgentManagerDialog(QtWidgets.QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Manage Agents")

        self.list = QtWidgets.QListWidget()
        self.list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        for name in AGENT_REGISTRY:
            item = QtWidgets.QListWidgetItem(name)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            state = QtCore.Qt.Checked if AGENT_ACTIVE.get(name, True) else QtCore.Qt.Unchecked
            item.setCheckState(state)
            self.list.addItem(item)

        save_btn = QtWidgets.QPushButton("Save")
        save_btn.clicked.connect(self.save)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.list)
        layout.addWidget(save_btn)

    def save(self) -> None:
        for i in range(self.list.count()):
            item = self.list.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                activate_agent(item.text())
            else:
                deactivate_agent(item.text())
        QtWidgets.QMessageBox.information(self, "Agents", "Saved")
        self.accept()
