from __future__ import annotations

from pathlib import Path

from core.tool_store import load_tools
from core.tools import register_tool


class Plugin:
    def __init__(self, path: Path = Path("tools.yaml")) -> None:
        self.path = Path(path)

    def register(self, app) -> None:  # pragma: no cover - dynamic loading
        for spec in load_tools(self.path):
            name = spec.get("name")
            if not name:
                continue
            register_tool(name, spec)
