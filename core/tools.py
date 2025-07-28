from __future__ import annotations

from typing import Dict
import subprocess

TOOL_REGISTRY: Dict[str, dict] = {}


def register_tool(name: str, spec: dict) -> None:
    """Register a tool definition in the global registry."""
    TOOL_REGISTRY[name] = spec


def is_tool_registered(name: str) -> bool:
    """Return True if the tool name is registered."""
    return name in TOOL_REGISTRY


def get_tool(name: str) -> dict | None:
    """Return a tool specification from the registry."""
    return TOOL_REGISTRY.get(name)


def run_tool(name: str, params: str = "") -> str:
    """Execute a registered tool and return its output."""
    spec = get_tool(name)
    if not spec:
        raise ValueError(f"Tool {name} not registered")
    command = spec.get("command", "")
    base_params = spec.get("params", "")
    cmd = f"{command} {base_params} {params}".strip()
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result.stdout.strip() or result.stderr.strip()
