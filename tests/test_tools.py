from core.tool_store import add_tool, load_tools, remove_tool
from plugins.tools_loader import Plugin
from core.tools import TOOL_REGISTRY, register_tool, run_tool
import pytest
try:
    from PySide6 import QtWidgets
    from gui.tool_editor import ToolEditorDialog
except Exception as exc:  # pragma: no cover - skip if Qt not installed
    QtWidgets = None


def test_add_tool(tmp_path):
    path = tmp_path / "tools.yaml"
    add_tool({"name": "fmt", "description": "", "command": "black", "params": ""}, path)
    tools = load_tools(path)
    assert tools[0]["name"] == "fmt"


def test_plugin_register_tool(tmp_path):
    path = tmp_path / "tools.yaml"
    add_tool({"name": "lint", "description": "", "command": "flake8", "params": ""}, path)
    plugin = Plugin(path)
    plugin.register(None)
    assert "lint" in TOOL_REGISTRY


def test_remove_tool(tmp_path):
    path = tmp_path / "tools.yaml"
    add_tool({"name": "fmt", "description": "", "command": "black", "params": ""}, path)
    remove_tool("fmt", path)
    assert load_tools(path) == []


def test_run_tool_echo(tmp_path):
    TOOL_REGISTRY.clear()
    register_tool("echo", {"command": "echo", "params": ""})
    output = run_tool("echo", "hello")
    assert output.strip() == "hello"


def test_tool_editor_registers(monkeypatch):
    if QtWidgets is None:
        pytest.skip("Qt not available")
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    TOOL_REGISTRY.clear()
    saved = {}

    def fake_add(tool):
        saved.update(tool)

    monkeypatch.setattr("gui.tool_editor.add_tool", fake_add)
    monkeypatch.setattr(QtWidgets.QMessageBox, "information", lambda *a, **k: None)
    dlg = ToolEditorDialog()
    dlg.name_edit.setText("mytool")
    dlg.save()
    assert saved.get("name") == "mytool"
    assert "mytool" in TOOL_REGISTRY
