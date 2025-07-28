import sqlite3
from db import (
    connect,
    create_user,
    authenticate_user,
    create_project,
    delete_project,
)
from pathlib import Path


def setup_db(tmp_path: Path) -> sqlite3.Connection:
    from db.init_db import init_db

    db_path = tmp_path / "test.db"
    init_db(db_path)
    return connect(db_path)


def test_bcrypt_registration_and_login(tmp_path):
    conn = setup_db(tmp_path)
    create_user(conn, "alice", "secret", role="admin")
    uid, role = authenticate_user(conn, "alice", "secret")
    assert uid is not None and role == "admin"
    row = conn.execute("SELECT password_hash FROM users WHERE id=?", (uid,)).fetchone()
    assert row["password_hash"].startswith("$2b$")

    # simulate legacy sha256 hash
    legacy = conn.execute("SELECT id FROM users WHERE username='alice'").fetchone()["id"]
    legacy_hash = "2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b"
    conn.execute(
        "UPDATE users SET password_hash=? WHERE id=?",
        (legacy_hash, legacy),
    )
    uid2, _ = authenticate_user(conn, "alice", "secret")
    assert uid2 == legacy
    row = conn.execute("SELECT password_hash FROM users WHERE id=?", (legacy,)).fetchone()
    assert row["password_hash"].startswith("$2b$")


def test_delete_project(tmp_path):
    conn = setup_db(tmp_path)
    create_user(conn, "admin", "x", role="admin")
    create_project(conn, 1, "proj")
    row = conn.execute("SELECT id FROM projects WHERE name='proj'").fetchone()
    pid = row["id"]
    delete_project(conn, pid)
    row = conn.execute("SELECT id FROM projects WHERE id=?", (pid,)).fetchone()
    assert row is None


def test_dashboard_permissions(monkeypatch, tmp_path):
    import pytest
    try:
        from PySide6 import QtWidgets
    except Exception as exc:
        pytest.skip(str(exc))
    from gui.dashboard import Dashboard

    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])

    conn = setup_db(tmp_path)
    create_user(conn, "bob", "pwd", role="user")
    create_project(conn, 1, "proj")
    row = conn.execute("SELECT id FROM projects WHERE name='proj'").fetchone()
    pid = row["id"]

    dash = Dashboard(conn, user_id=1, username="bob", role="user")
    dash.selected_project_id = lambda: pid

    warnings = []
    monkeypatch.setattr(QtWidgets.QMessageBox, "warning", lambda *a, **k: warnings.append(True))

    dash.delete_project()
    assert warnings
    row = conn.execute("SELECT id FROM projects WHERE id=?", (pid,)).fetchone()
    assert row is not None
