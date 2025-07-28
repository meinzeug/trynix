from __future__ import annotations

from PySide6 import QtWidgets

from db import create_project, get_projects
from core import AIController
from .chat import ChatWindow
from .codeviewer import CodeViewer


class Dashboard(QtWidgets.QMainWindow):
    def __init__(self, conn, username: str) -> None:
        super().__init__()
        self.conn = conn
        self.username = username
        self.setWindowTitle(f"trynix - {username}")

        self.project_list = QtWidgets.QListWidget()
        self.new_btn = QtWidgets.QPushButton("New Project")
        self.chat_btn = QtWidgets.QPushButton("Open Chat")
        self.code_btn = QtWidgets.QPushButton("View Code")
        self.run_btn = QtWidgets.QPushButton("Run AI")

        central = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(central)
        layout.addWidget(QtWidgets.QLabel(f"Logged in as {username}"))
        layout.addWidget(self.project_list)
        layout.addWidget(self.new_btn)
        layout.addWidget(self.run_btn)
        layout.addWidget(self.chat_btn)
        layout.addWidget(self.code_btn)
        self.setCentralWidget(central)

        self.new_btn.clicked.connect(self.create_project)
        self.run_btn.clicked.connect(self.start_ai)
        self.chat_btn.clicked.connect(self.open_chat)
        self.code_btn.clicked.connect(self.open_code)
        self.load_projects()

    def load_projects(self) -> None:
        self.projects = get_projects(self.conn)
        self.project_list.clear()
        for row in self.projects:
            self.project_list.addItem(row["name"])

    def create_project(self) -> None:
        name, ok = QtWidgets.QInputDialog.getText(self, "New Project", "Project name:")
        if ok and name:
            create_project(self.conn, name)
            self.load_projects()

    def selected_project_id(self) -> int | None:
        row = self.project_list.currentRow()
        if row < 0:
            return None
        return self.projects[row]["id"]

    def open_chat(self) -> None:
        project_id = self.selected_project_id()
        if project_id is not None:
            win = ChatWindow(self.conn, project_id)
            win.show()

    def open_code(self) -> None:
        project_id = self.selected_project_id()
        if project_id is not None:
            win = CodeViewer(self.conn, project_id)
            win.show()

    def start_ai(self) -> None:
        project_id = self.selected_project_id()
        if project_id is None:
            return
        idea, ok = QtWidgets.QInputDialog.getText(self, "Project Idea", "Describe project idea:")
        if ok and idea:
            controller = AIController(self.conn)
            controller.run_project(project_id, idea)
            QtWidgets.QMessageBox.information(self, "AI", "Project completed")
