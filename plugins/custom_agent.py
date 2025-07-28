"""Example plugin providing a simple custom agent."""

from __future__ import annotations

from core.agents import BaseAgent, register_agent
from db import add_message


class EchoAgent(BaseAgent):
    """Agent that echoes any message back to the log."""

    def echo(self, project_id: int, text: str) -> None:
        add_message(self.conn, project_id, self.name, text)


class Plugin:
    def register(self, app) -> None:  # pragma: no cover - plugin registration
        register_agent("echo", EchoAgent)
