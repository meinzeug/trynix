from __future__ import annotations

from PySide6 import QtWidgets, QtCore

from db import get_tasks


class StatusWindow(QtWidgets.QWidget):
    """Display live status of all tasks for a project."""

    def __init__(self, conn, project_id: int) -> None:
        super().__init__()
        self.conn = conn
        self.project_id = project_id
        self.setWindowTitle("Agent Status")

        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Agent", "Task", "Status"])

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.table)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.load_status)
        self.timer.start(1000)

        self.load_status()

    def load_status(self) -> None:
        tasks = get_tasks(self.conn, self.project_id)
        self.table.setRowCount(len(tasks))
        for row_index, row in enumerate(tasks):
            self.table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(row["agent"]))
            self.table.setItem(row_index, 1, QtWidgets.QTableWidgetItem(row["description"]))
            self.table.setItem(row_index, 2, QtWidgets.QTableWidgetItem(row["status"]))

