from __future__ import annotations

from PySide6 import QtWidgets

from db import create_project, get_projects
from core import AIController
from services import start_share, stop_share
from .chat import ChatWindow
from .codeviewer import CodeViewer
from .status import StatusWindow
from .admin import AdminWindow
from .settings import SettingsWindow


class Dashboard(QtWidgets.QMainWindow):
    def __init__(self, conn, user_id: int, username: str, role: str) -> None:
        super().__init__()
        self.conn = conn
        self.username = username
        self.user_id = user_id
        self.role = role
        self.setWindowTitle(f"trynix - {username}")

        self.project_list = QtWidgets.QListWidget()
        self.new_btn = QtWidgets.QPushButton("New Project")
        self.chat_btn = QtWidgets.QPushButton("Open Chat")
        self.code_btn = QtWidgets.QPushButton("View Code")
        self.status_btn = QtWidgets.QPushButton("View Status")
        self.run_btn = QtWidgets.QPushButton("Run AI")
        self.share_btn = QtWidgets.QPushButton("Share Project")
        self.settings_btn = QtWidgets.QPushButton("Settings")
        self.admin_btn = QtWidgets.QPushButton("Admin Panel")

        central = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(central)
        layout.addWidget(QtWidgets.QLabel(f"Logged in as {username}"))
        layout.addWidget(self.project_list)
        layout.addWidget(self.new_btn)
        layout.addWidget(self.run_btn)
        layout.addWidget(self.share_btn)
        layout.addWidget(self.chat_btn)
        layout.addWidget(self.code_btn)
        layout.addWidget(self.status_btn)
        layout.addWidget(self.settings_btn)
        if role == "admin":
            layout.addWidget(self.admin_btn)
        self.setCentralWidget(central)

        self.new_btn.clicked.connect(self.create_project)
        self.run_btn.clicked.connect(self.start_ai)
        self.share_btn.clicked.connect(self.share_project)
        self.chat_btn.clicked.connect(self.open_chat)
        self.code_btn.clicked.connect(self.open_code)
        self.status_btn.clicked.connect(self.view_status)
        self.settings_btn.clicked.connect(self.open_settings)
        self.admin_btn.clicked.connect(self.open_admin)
        self.load_projects()
        self._share_server = None

    def load_projects(self) -> None:
        self.projects = get_projects(self.conn, self.user_id, self.role)
        self.project_list.clear()
        for row in self.projects:
            self.project_list.addItem(row["name"])

    def create_project(self) -> None:
        name, ok = QtWidgets.QInputDialog.getText(self, "New Project", "Project name:")
        if ok and name:
            create_project(self.conn, self.user_id, name)
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

    def view_status(self) -> None:
        project_id = self.selected_project_id()
        if project_id is not None:
            win = StatusWindow(self.conn, project_id)
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

    def share_project(self) -> None:
        project_id = self.selected_project_id()
        if project_id is None:
            return
        if self._share_server is not None:
            QtWidgets.QMessageBox.information(self, "Share", "Project is already being shared")
            return
        server, thread, tmpdir, url = start_share(self.conn, project_id)
        self._share_server = (server, thread, tmpdir)
        QtWidgets.QMessageBox.information(self, "Share", f"Project available at {url}\nServer stops when application closes")

    def open_settings(self) -> None:
        win = SettingsWindow()
        win.exec()

    def open_admin(self) -> None:
        win = AdminWindow(self.conn)
        win.show()

    def closeEvent(self, event) -> None:
        if self._share_server is not None:
            stop_share(*self._share_server)
            self._share_server = None
        super().closeEvent(event)
