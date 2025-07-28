from __future__ import annotations

from pathlib import Path
import sqlite3
import hashlib


def connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def create_user(conn: sqlite3.Connection, username: str, password: str, role: str = "user") -> None:
    password_hash = hash_password(password)
    with conn:
        conn.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (username, password_hash, role),
        )


def verify_user(conn: sqlite3.Connection, username: str, password: str) -> bool:
    row = conn.execute(
        "SELECT password_hash FROM users WHERE username=?",
        (username,),
    ).fetchone()
    if row is None:
        return False
    return row["password_hash"] == hash_password(password)


def create_project(conn: sqlite3.Connection, name: str, description: str = "") -> None:
    with conn:
        conn.execute(
            "INSERT INTO projects (name, description, status) VALUES (?, ?, ?)",
            (name, description, "new"),
        )


def get_projects(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return list(conn.execute("SELECT id, name FROM projects"))
