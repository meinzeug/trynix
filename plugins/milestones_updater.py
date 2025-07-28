from __future__ import annotations

from pathlib import Path

from codex.update_milestones import update_file


class Plugin:
    """Plugin to automatically update milestones on startup."""

    def register(self, app) -> None:  # pragma: no cover - side effect
        update_file(Path("codex/daten/milestones.md"))
