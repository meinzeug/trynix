from __future__ import annotations

from pathlib import Path

from core.agent_store import load_agents
from core.agents import BaseAgent, register_agent


class Plugin:
    def __init__(self, path: Path = Path("agents.yaml")) -> None:
        self.path = Path(path)

    def register(self, app) -> None:  # pragma: no cover - dynamic loading
        for spec in load_agents(self.path):
            name = spec.get("name")
            if not name:
                continue

            class YAMLAgent(BaseAgent):
                def info(self) -> str:  # pragma: no cover - simple helper
                    return spec.get("description", "")

            register_agent(name, YAMLAgent)

