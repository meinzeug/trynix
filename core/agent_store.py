from __future__ import annotations

from pathlib import Path
from typing import List, Dict
import yaml

AGENTS_FILE = Path("agents.yaml")


def load_agents(path: Path = AGENTS_FILE) -> List[Dict[str, str]]:
    """Load agent definitions from YAML."""
    if not Path(path).exists():
        return []
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return data or []


def save_agents(agents: List[Dict[str, str]], path: Path = AGENTS_FILE) -> None:
    """Write agent definitions to YAML."""
    Path(path).write_text(
        yaml.safe_dump(agents, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def add_agent(agent: Dict[str, str], path: Path = AGENTS_FILE) -> None:
    """Append a new agent definition, ensuring unique names."""
    agents = load_agents(path)
    if any(a.get("name") == agent.get("name") for a in agents):
        raise ValueError("Agent name already exists")
    agents.append(agent)
    save_agents(agents, path)
