from __future__ import annotations

from typing import Dict

TOOL_REGISTRY: Dict[str, dict] = {}


def register_tool(name: str, spec: dict) -> None:
    """Register a tool definition in the global registry."""
    TOOL_REGISTRY[name] = spec
