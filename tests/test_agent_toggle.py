import sqlite3
from core.agents import (
    register_agent,
    activate_agent,
    deactivate_agent,
    is_agent_active,
    AGENT_REGISTRY,
)
from core.controller import AIController, BaseAgent


class DummyAgent(BaseAgent):
    pass


def test_activate_deactivate():
    name = "dummy_toggle"
    register_agent(name, DummyAgent)
    assert is_agent_active(name)
    deactivate_agent(name)
    assert not is_agent_active(name)
    activate_agent(name)
    assert is_agent_active(name)


def test_controller_refresh():
    name = "dummy_ctrl"
    register_agent(name, DummyAgent)
    conn = sqlite3.connect(":memory:")
    ctrl = AIController(conn)
    assert name in ctrl.agents
    deactivate_agent(name)
    ctrl.refresh_agents()
    assert name not in ctrl.agents
