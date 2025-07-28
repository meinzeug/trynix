from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict
from pathlib import Path
import json

@dataclass
class RoadmapItem:
    title: str
    status: str = "open"
    tasks: List[Dict[str, str]] = field(default_factory=list)


def load_roadmap(path: Path) -> Dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data


def save_roadmap(data: Dict, path: Path) -> None:
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def mark_task_done(data: Dict, description: str) -> None:
    for ms in data.get("milestones", []):
        for task in ms.get("tasks", []):
            if task.get("title") == description:
                task["status"] = "done"
        if all(t.get("status") == "done" for t in ms.get("tasks", [])):
            ms["status"] = "done"
