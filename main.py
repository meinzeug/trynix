from __future__ import annotations

from PySide6 import QtWidgets

from core import CONFIG
from core.logger import init_logging
from db import connect
from db.init_db import init_db
from gui import Dashboard, LoginWindow
from core.plugins import load_plugins


def main() -> None:
    init_logging(CONFIG.log_dir)
    init_db(CONFIG.db_path)
    conn = connect(CONFIG.db_path)

    app = QtWidgets.QApplication([])
    load_plugins(app)
    login = LoginWindow(conn)
    if login.exec() == QtWidgets.QDialog.Accepted and login.username:
        window = Dashboard(conn, login.user_id, login.username, login.role or "user")
        window.show()
        app.exec()
    conn.close()


if __name__ == "__main__":
    main()
