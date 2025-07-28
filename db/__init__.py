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


def add_message(
    conn: sqlite3.Connection, project_id: int, sender: str, message: str
) -> None:
    """Store a chat message for a project."""
    with conn:
        conn.execute(
            "INSERT INTO messages (project_id, sender, message) VALUES (?, ?, ?)",
            (project_id, sender, message),
        )


def get_messages(conn: sqlite3.Connection, project_id: int) -> list[sqlite3.Row]:
    """Return chat history for a project ordered by insertion."""
    return list(
        conn.execute(
            "SELECT sender, message, timestamp FROM messages WHERE project_id=? "
            "ORDER BY id",
            (project_id,),
        )
    )


def get_code_files(conn: sqlite3.Connection, project_id: int) -> list[sqlite3.Row]:
    """Return list of code files belonging to a project."""
    return list(
        conn.execute(
            "SELECT id, path, content FROM code_files WHERE project_id=?",
            (project_id,),
        )
    )

def add_code_file(conn: sqlite3.Connection, project_id: int, path: str, content: str) -> None:
    """Store a generated code file for a project."""
    with conn:
        conn.execute(
            "INSERT INTO code_files (project_id, path, content) VALUES (?, ?, ?)",
            (project_id, path, content),
        )


def create_task(
    conn: sqlite3.Connection,
    project_id: int,
    agent: str,
    description: str,
    status: str = "pending",
) -> int:
    """Create a new task and return its ID."""
    with conn:
        cur = conn.execute(
            "INSERT INTO tasks (project_id, agent, description, status) VALUES (?, ?, ?, ?)",
            (project_id, agent, description, status),
        )
        return cur.lastrowid


def get_tasks(conn: sqlite3.Connection, project_id: int) -> list[sqlite3.Row]:
    return list(
        conn.execute(
            "SELECT id, agent, description, status FROM tasks WHERE project_id=?",
            (project_id,),
        )
    )


def update_task_status(conn: sqlite3.Connection, task_id: int, status: str) -> None:
    with conn:
        conn.execute(
            "UPDATE tasks SET status=? WHERE id=?",
            (status, task_id),
        )

