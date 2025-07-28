from __future__ import annotations

from PySide6 import QtWidgets

from core.config import Config
from core.logger import init_logging
from db import connect
from db.init_db import init_db
from gui import Dashboard, LoginWindow


def main() -> None:
    config = Config.load("config.json")
    init_logging(config.log_dir)
    init_db(config.db_path)
    conn = connect(config.db_path)

    app = QtWidgets.QApplication([])
    login = LoginWindow(conn)
    if login.exec() == QtWidgets.QDialog.Accepted and login.username:
        window = Dashboard(conn, login.username)
        window.show()
        app.exec()
    conn.close()


if __name__ == "__main__":
    main()
