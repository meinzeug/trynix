from __future__ import annotations

from db import add_message, get_tasks, create_task, update_task_status
from .agents import Queen, HiveWorker, TestWorker
from services import run_flow


class AIController:
    """Orchestrate Queen and Hive Worker for a project."""

    def __init__(self, conn) -> None:
        self.conn = conn
        self.queen = Queen(conn, "queen")
        self.worker = HiveWorker(conn, "hive")
        self.tester = TestWorker(conn, "tester")

    def run_project(self, project_id: int, idea: str) -> None:
        """Plan tasks with Queen and execute them with a single worker."""
        add_message(self.conn, project_id, "system", f"Starting project: {idea}")
        self.queen.plan_project(project_id, idea)
        for task in get_tasks(self.conn, project_id):
            code = self.worker.execute_task(task["id"], project_id, task["description"])
            test_id = create_task(
                self.conn,
                project_id,
                "test",
                f"Tests for task {task['id']}",
                status="running",
            )
            status = self.tester.run_tests(project_id, task["id"], code)
            update_task_status(self.conn, test_id, status)

        # run additional orchestration via Claude-Flow CLI
        try:
            output = run_flow(["npx", "claude-flow@alpha", "hive-mind", "wizard", "--force"])
            add_message(self.conn, project_id, "claude-flow", output)
        except Exception as exc:  # subprocess.CalledProcessError etc.
            add_message(self.conn, project_id, "error", str(exc))

        add_message(self.conn, project_id, "system", "All tasks completed")
