from core.context import load_context, save_context, append_entry, ContextState
from db.init_db import init_db
from db import load_context_db, save_context_db
import sqlite3


def test_context_file_ops(tmp_path):
    path = tmp_path / "ctx.json"
    state = load_context(path)
    assert state.history == []
    state.history.append({"msg": "hi"})
    save_context(state, path)
    state2 = load_context(path)
    assert state2.history[0]["msg"] == "hi"


def test_context_db(tmp_path):
    db_path = tmp_path / "db.sqlite"
    init_db(db_path)
    conn = sqlite3.connect(db_path)
    save_context_db(conn, '{"foo": 1}')
    data = load_context_db(conn)
    assert "foo" in data
