from __future__ import annotations

from typing import Dict

TOOL_REGISTRY: Dict[str, dict] = {}


def register_tool(name: str, spec: dict) -> None:
    """Register a tool definition in the global registry."""
    TOOL_REGISTRY[name] = spec


def is_tool_registered(name: str) -> bool:
    """Return True if the tool name is registered."""
    return name in TOOL_REGISTRY
