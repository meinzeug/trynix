from __future__ import annotations

from PySide6 import QtWidgets

from db import create_user, authenticate_user


class LoginWindow(QtWidgets.QDialog):
    def __init__(self, conn) -> None:
        super().__init__()
        self.conn = conn
        self.setWindowTitle("trynix Login")
        self.username_edit = QtWidgets.QLineEdit()
        self.password_edit = QtWidgets.QLineEdit()
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_btn = QtWidgets.QPushButton("Login")
        self.register_btn = QtWidgets.QPushButton("Register")

        form = QtWidgets.QFormLayout()
        form.addRow("Username", self.username_edit)
        form.addRow("Password", self.password_edit)

        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addWidget(self.login_btn)
        btn_layout.addWidget(self.register_btn)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(btn_layout)

        self.login_btn.clicked.connect(self.handle_login)
        self.register_btn.clicked.connect(self.handle_register)
        self.username: str | None = None
        self.user_id: int | None = None
        self.role: str | None = None

    def handle_login(self) -> None:
        uid, role = authenticate_user(
            self.conn, self.username_edit.text(), self.password_edit.text()
        )
        if uid is not None:
            self.username = self.username_edit.text()
            self.user_id = uid
            self.role = role
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid credentials")

    def handle_register(self) -> None:
        try:
            create_user(self.conn, self.username_edit.text(), self.password_edit.text())
            QtWidgets.QMessageBox.information(self, "Registered", "User created")
        except Exception as exc:  # sqlite3.IntegrityError etc.
            QtWidgets.QMessageBox.warning(self, "Error", str(exc))
