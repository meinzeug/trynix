from core.agent_store import add_agent, load_agents
from plugins.agents_loader import Plugin
from core.agents import AGENT_REGISTRY
from core.tools import TOOL_REGISTRY, register_tool
import pytest
try:
    from PySide6 import QtWidgets
    from gui.agent_creator import AgentCreatorDialog
except Exception as exc:  # pragma: no cover - skip if no Qt
    QtWidgets = None


def test_add_agent(tmp_path):
    path = tmp_path / "agents.yaml"
    add_agent({"name": "alpha", "description": "", "specialization": "", "abilities": ""}, path)
    agents = load_agents(path)
    assert agents[0]["name"] == "alpha"


def test_plugin_register(tmp_path):
    path = tmp_path / "agents.yaml"
    add_agent({"name": "beta", "description": "", "specialization": "", "abilities": ""}, path)
    plugin = Plugin(path)
    plugin.register(None)
    assert "beta" in AGENT_REGISTRY


def test_plugin_unknown_tool(tmp_path):
    path = tmp_path / "agents.yaml"
    add_agent({"name": "delta", "tools": "missing"}, path)
    plugin = Plugin(path)
    with pytest.raises(ValueError):
        plugin.register(None)


def test_agent_with_tools(tmp_path):
    path = tmp_path / "agents.yaml"
    add_agent({"name": "gamma", "description": "", "specialization": "", "abilities": "", "tools": "lint"}, path)
    agents = load_agents(path)
    assert agents[0]["tools"] == "lint"


def test_agent_creator_lists_tools(monkeypatch):
    if QtWidgets is None:
        pytest.skip("Qt not available")
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    TOOL_REGISTRY.clear()
    register_tool("fmt", {})
    dlg = AgentCreatorDialog()
    names = [dlg.tools_list.item(i).text() for i in range(dlg.tools_list.count())]
    assert "fmt" in names


def test_agent_creator_save(monkeypatch):
    if QtWidgets is None:
        pytest.skip("Qt not available")
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    TOOL_REGISTRY.clear()
    register_tool("lint", {})
    saved = {}

    def fake_add(agent):
        saved.update(agent)

    monkeypatch.setattr("gui.agent_creator.add_agent", fake_add)
    monkeypatch.setattr(QtWidgets.QMessageBox, "information", lambda *a, **k: None)
    dlg = AgentCreatorDialog()
    dlg.name_edit.setText("agent")
    dlg.tools_list.item(0).setSelected(True)
    dlg.save()
    assert saved.get("tools") == "lint"
