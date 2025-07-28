from __future__ import annotations

from PySide6 import QtWidgets

from db import (
    get_tasks,
    create_task,
    update_task_description,
)


class TaskManagerWindow(QtWidgets.QWidget):
    """Window to edit and add tasks for a project."""

    def __init__(self, conn, project_id: int) -> None:
        super().__init__()
        self.conn = conn
        self.project_id = project_id
        self.setWindowTitle("Task Manager")

        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Agent", "Description", "Status"])

        self.add_btn = QtWidgets.QPushButton("Add Task")
        self.edit_btn = QtWidgets.QPushButton("Edit Selected")

        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.edit_btn)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.table)
        layout.addLayout(btn_layout)

        self.add_btn.clicked.connect(self.add_task)
        self.edit_btn.clicked.connect(self.edit_task)

        self.load_tasks()

    #
    # helpers
    #
    def load_tasks(self) -> None:
        self.tasks = get_tasks(self.conn, self.project_id)
        self.table.setRowCount(len(self.tasks))
        for idx, row in enumerate(self.tasks):
            self.table.setItem(idx, 0, QtWidgets.QTableWidgetItem(row["agent"]))
            self.table.setItem(
                idx, 1, QtWidgets.QTableWidgetItem(row["description"])
            )
            self.table.setItem(idx, 2, QtWidgets.QTableWidgetItem(row["status"]))

    def add_task(self) -> None:
        text, ok = QtWidgets.QInputDialog.getText(self, "Add Task", "Description:")
        if ok and text:
            create_task(self.conn, self.project_id, "hive", text)
            self.load_tasks()

    def edit_task(self) -> None:
        row = self.table.currentRow()
        if row < 0:
            return
        task = self.tasks[row]
        text, ok = QtWidgets.QInputDialog.getText(
            self, "Edit Task", "Description:", text=task["description"]
        )
        if ok and text:
            update_task_description(self.conn, task["id"], text)
            self.load_tasks()

