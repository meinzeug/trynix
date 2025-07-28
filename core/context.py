from __future__ import annotations

from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Any, Dict
import sqlite3
import json

CONTEXT_FILE = Path("context_state.json")


@dataclass
class ContextState:
    """Data container for the global application context."""

    history: list = field(default_factory=list)
    agents: Dict[str, Any] = field(default_factory=dict)
    task_flow: list = field(default_factory=list)
    handoffs: list = field(default_factory=list)
    user_actions: list = field(default_factory=list)


DEFAULT_STATE = ContextState()


def load_context(path: Path = CONTEXT_FILE, conn: sqlite3.Connection | None = None) -> ContextState:
    """Load context state from JSON file or DB."""
    if conn is not None:
        from db import load_context_db

        data_json = load_context_db(conn)
        data = json.loads(data_json) if data_json else {}
    elif path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
    else:
        data = {}
    base = asdict(DEFAULT_STATE)
    base.update(data)
    return ContextState(**base)


def save_context(
    state: ContextState,
    path: Path = CONTEXT_FILE,
    conn: sqlite3.Connection | None = None,
) -> None:
    """Save context state to JSON file and optionally DB."""
    data = json.dumps(asdict(state), indent=2)
    path.write_text(data, encoding="utf-8")
    if conn is not None:
        from db import save_context_db

        save_context_db(conn, data)


def append_entry(
    section: str,
    entry: Any,
    path: Path = CONTEXT_FILE,
    conn: sqlite3.Connection | None = None,
) -> ContextState:
    """Append an entry to a section and persist the state."""
    state = load_context(path, conn)
    if not hasattr(state, section):
        raise ValueError(f"Unknown section: {section}")
    attr = getattr(state, section)
    if section == "agents" and isinstance(entry, dict):
        attr.update(entry)
    else:
        attr.append(entry)
    setattr(state, section, attr)
    save_context(state, path, conn)
    return state
