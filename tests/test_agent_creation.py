from core.agent_store import add_agent, load_agents
from plugins.agents_loader import Plugin
from core.agents import AGENT_REGISTRY


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


def test_agent_with_tools(tmp_path):
    path = tmp_path / "agents.yaml"
    add_agent({"name": "gamma", "description": "", "specialization": "", "abilities": "", "tools": "lint"}, path)
    agents = load_agents(path)
    assert agents[0]["tools"] == "lint"
