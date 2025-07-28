from core.tool_store import add_tool, load_tools, remove_tool
from plugins.tools_loader import Plugin
from core.tools import TOOL_REGISTRY, register_tool, run_tool


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
