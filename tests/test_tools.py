from core.tool_store import add_tool, load_tools
from plugins.tools_loader import Plugin
from core.tools import TOOL_REGISTRY


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
