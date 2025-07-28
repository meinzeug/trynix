from __future__ import annotations

from PySide6 import QtWidgets

from db import create_project, get_projects


class Dashboard(QtWidgets.QMainWindow):
    def __init__(self, conn, username: str) -> None:
        super().__init__()
        self.conn = conn
        self.username = username
        self.setWindowTitle(f"trynix - {username}")

        self.project_list = QtWidgets.QListWidget()
        self.new_btn = QtWidgets.QPushButton("New Project")

        central = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(central)
        layout.addWidget(QtWidgets.QLabel(f"Logged in as {username}"))
        layout.addWidget(self.project_list)
        layout.addWidget(self.new_btn)
        self.setCentralWidget(central)

        self.new_btn.clicked.connect(self.create_project)
        self.load_projects()

    def load_projects(self) -> None:
        self.project_list.clear()
        for row in get_projects(self.conn):
            self.project_list.addItem(row["name"])

    def create_project(self) -> None:
        name, ok = QtWidgets.QInputDialog.getText(self, "New Project", "Project name:")
        if ok and name:
            create_project(self.conn, name)
            self.load_projects()
