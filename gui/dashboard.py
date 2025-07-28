from __future__ import annotations

from PySide6 import QtWidgets, QtCore
import threading

from db import create_project, get_projects, get_project, set_project_workspace
from core import AIController
from .taskmanager import TaskManagerWindow
from services import start_share, stop_share
from .chat import ChatWindow
from .codeviewer import CodeViewer
from .workspace import WorkspaceViewer
from .roadmap import RoadmapWindow
from .status import StatusWindow
from .admin import AdminWindow
from .settings import SettingsWindow
from .wand import WandWindow
from core.config import CONFIG
from pathlib import Path
import datetime


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
        self.workspace_btn = QtWidgets.QPushButton("Workspace")
        self.roadmap_btn = QtWidgets.QPushButton("Roadmap")
        self.status_btn = QtWidgets.QPushButton("View Status")
        self.tasks_btn = QtWidgets.QPushButton("Manage Tasks")
        self.run_btn = QtWidgets.QPushButton("Run AI")
        self.pause_btn = QtWidgets.QPushButton("Pause")
        self.resume_btn = QtWidgets.QPushButton("Resume")
        self.share_btn = QtWidgets.QPushButton("Share Project")
        self.wand_btn = QtWidgets.QPushButton("🪄")
        self.wand_btn.setToolTip("Lass die Queen neue Features vorschlagen")
        self.status_label = QtWidgets.QLabel("AI Status: Idle")
        self.settings_btn = QtWidgets.QPushButton("Settings")
        self.admin_btn = QtWidgets.QPushButton("Admin Panel")

        central = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(central)
        layout.addWidget(QtWidgets.QLabel(f"Logged in as {username}"))
        layout.addWidget(self.project_list)
        layout.addWidget(self.new_btn)
        layout.addWidget(self.run_btn)
        layout.addWidget(self.pause_btn)
        layout.addWidget(self.resume_btn)
        layout.addWidget(self.share_btn)
        layout.addWidget(self.wand_btn)
        layout.addWidget(self.chat_btn)
        layout.addWidget(self.code_btn)
        layout.addWidget(self.workspace_btn)
        layout.addWidget(self.roadmap_btn)
        layout.addWidget(self.tasks_btn)
        layout.addWidget(self.status_btn)
        layout.addWidget(self.status_label)
        layout.addWidget(self.settings_btn)
        if role == "admin":
            layout.addWidget(self.admin_btn)
        self.setCentralWidget(central)

        self.new_btn.clicked.connect(self.create_project)
        self.run_btn.clicked.connect(self.start_ai)
        self.pause_btn.clicked.connect(self.pause_ai)
        self.resume_btn.clicked.connect(self.resume_ai)
        self.tasks_btn.clicked.connect(self.manage_tasks)
        self.share_btn.clicked.connect(self.share_project)
        self.wand_btn.clicked.connect(self.open_wand)
        self.chat_btn.clicked.connect(self.open_chat)
        self.code_btn.clicked.connect(self.open_code)
        self.workspace_btn.clicked.connect(self.open_workspace)
        self.roadmap_btn.clicked.connect(self.open_roadmap)
        self.status_btn.clicked.connect(self.view_status)
        self.settings_btn.clicked.connect(self.open_settings)
        self.admin_btn.clicked.connect(self.open_admin)
        self.load_projects()
        self._share_server = None
        self.controller: AIController | None = None
        self._thread: threading.Thread | None = None
        self._status_timer = QtCore.QTimer(self)
        self._status_timer.timeout.connect(self.update_status)
        self._status_timer.start(500)

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

    def open_workspace(self) -> None:
        project_id = self.selected_project_id()
        if project_id is not None:
            row = get_project(self.conn, project_id)
            if row and row["workspace"]:
                win = WorkspaceViewer(Path(row["workspace"]))
                win.show()
            else:
                QtWidgets.QMessageBox.information(
                    self, "Workspace", "No workspace available for this project"
                )

    def open_wand(self) -> None:
        project_id = self.selected_project_id()
        if project_id is not None:
            win = WandWindow(self.conn, project_id)
            win.show()

    def open_roadmap(self) -> None:
        project_id = self.selected_project_id()
        if project_id is not None:
            win = RoadmapWindow(self.conn, project_id)
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
            if self.controller and self.controller.running:
                QtWidgets.QMessageBox.information(self, "AI", "AI already running")
                return
            self.controller = AIController(self.conn)
            # create workspace directory
            row = get_project(self.conn, project_id)
            name = row["name"] if row else str(project_id)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            ws_root = CONFIG.workspace_dir
            ws_root.mkdir(exist_ok=True)
            workspace = ws_root / f"{name}-{timestamp}"
            workspace.mkdir(parents=True, exist_ok=True)
            set_project_workspace(self.conn, project_id, str(workspace))
            self._thread = threading.Thread(
                target=self.controller.run_project,
                args=(project_id, idea, workspace),
                daemon=True,
            )
            self._thread.start()

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

    def pause_ai(self) -> None:
        if self.controller:
            self.controller.pause()

    def resume_ai(self) -> None:
        if self.controller:
            self.controller.resume()

    def manage_tasks(self) -> None:
        project_id = self.selected_project_id()
        if project_id is not None:
            win = TaskManagerWindow(self.conn, project_id)
            win.show()

    def update_status(self) -> None:
        if self.controller and self.controller.running:
            status = "Paused" if self.controller.is_paused() else "Running"
        else:
            status = "Idle"
        self.status_label.setText(f"AI Status: {status}")

    def open_admin(self) -> None:
        win = AdminWindow(self.conn)
        win.show()

    def closeEvent(self, event) -> None:
        if self._share_server is not None:
            stop_share(*self._share_server)
            self._share_server = None
        super().closeEvent(event)
