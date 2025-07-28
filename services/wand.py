from __future__ import annotations

from pathlib import Path
from typing import List, Dict

from .openrouter import send_prompt


def collect_context(workspace: Path) -> str:
    """Return a short summary of python files under the workspace."""
    parts = []
    if workspace.is_dir():
        for path in workspace.rglob('*.py'):
            parts.append(path.name)
    return "\n".join(parts)


def suggest_features(workspace: Path, milestones_path: Path) -> List[Dict[str, str]]:
    """Use OpenRouter to suggest new feature ideas based on the code base."""
    files = collect_context(workspace)
    milestones = milestones_path.read_text(encoding='utf-8') if milestones_path.exists() else ''
    prompt = (
        "You are the Queen AI of a software project. "
        "Based on the following code files and current milestones, propose 2-5 new "
        "feature ideas. Return each idea on a separate line in the form 'Title: Description'.\n"
        f"Code files:\n{files}\nMilestones:\n{milestones}"
    )
    response = send_prompt(prompt)
    ideas: List[Dict[str, str]] = []
    for line in response.splitlines():
        if ':' in line:
            title, desc = line.split(':', 1)
            ideas.append({'title': title.strip(' -'), 'description': desc.strip()})
    return ideas


def add_milestone(idea: Dict[str, str], path: Path) -> None:
    """Append a new milestone with a single task to the milestones file."""
    text = f"\n## {idea['title']}\n- [ ] {idea['description']}\n"
    with path.open('a', encoding='utf-8') as f:
        f.write(text)
