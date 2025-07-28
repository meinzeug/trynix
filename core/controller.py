from __future__ import annotations

from db import add_message, get_tasks
from .agents import Queen, HiveWorker


class AIController:
    """Orchestrate Queen and Hive Worker for a project."""

    def __init__(self, conn) -> None:
        self.conn = conn
        self.queen = Queen(conn, "queen")
        self.worker = HiveWorker(conn, "hive")

    def run_project(self, project_id: int, idea: str) -> None:
        """Plan tasks with Queen and execute them with a single worker."""
        add_message(self.conn, project_id, "system", f"Starting project: {idea}")
        self.queen.plan_project(project_id, idea)
        for task in get_tasks(self.conn, project_id):
            self.worker.execute_task(task["id"], project_id, task["description"])
        add_message(self.conn, project_id, "system", "All tasks completed")
