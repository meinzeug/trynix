from __future__ import annotations

from PySide6 import QtWidgets

from db import get_users, delete_user


class AdminWindow(QtWidgets.QWidget):
    """Simple user management window for admins."""

    def __init__(self, conn) -> None:
        super().__init__()
        self.conn = conn
        self.setWindowTitle("User Management")

        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Username", "Role"])

        self.refresh_btn = QtWidgets.QPushButton("Refresh")
        self.delete_btn = QtWidgets.QPushButton("Delete")

        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addWidget(self.refresh_btn)
        btn_layout.addWidget(self.delete_btn)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.table)
        layout.addLayout(btn_layout)

        self.refresh_btn.clicked.connect(self.load_users)
        self.delete_btn.clicked.connect(self.delete_selected)

        self.load_users()

    def load_users(self) -> None:
        users = get_users(self.conn)
        self.table.setRowCount(len(users))
        for row_index, row in enumerate(users):
            self.table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(str(row["id"])))
            self.table.setItem(row_index, 1, QtWidgets.QTableWidgetItem(row["username"]))
            self.table.setItem(row_index, 2, QtWidgets.QTableWidgetItem(row["role"]))

    def delete_selected(self) -> None:
        row = self.table.currentRow()
        if row < 0:
            return
        user_id_item = self.table.item(row, 0)
        if user_id_item is None:
            return
        user_id = int(user_id_item.text())
        delete_user(self.conn, user_id)
        self.load_users()
