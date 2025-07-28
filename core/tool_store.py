from __future__ import annotations

from pathlib import Path
from typing import List, Dict
import yaml

TOOLS_FILE = Path("tools.yaml")


def load_tools(path: Path = TOOLS_FILE) -> List[Dict[str, str]]:
    """Load tool definitions from YAML."""
    if not Path(path).exists():
        return []
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return data or []


def save_tools(tools: List[Dict[str, str]], path: Path = TOOLS_FILE) -> None:
    """Write tool definitions to YAML."""
    Path(path).write_text(
        yaml.safe_dump(tools, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def add_tool(tool: Dict[str, str], path: Path = TOOLS_FILE) -> None:
    """Append a new tool definition, ensuring unique names."""
    tools = load_tools(path)
    if any(t.get("name") == tool.get("name") for t in tools):
        raise ValueError("Tool name already exists")
    tools.append(tool)
    save_tools(tools, path)
