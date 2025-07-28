from __future__ import annotations

from db import (
    add_message,
    get_tasks,
    create_task,
    update_task_status,
    get_project,
)
from typing import Dict
from pathlib import Path

from .agents import (
    BaseAgent,
    AGENT_REGISTRY,
    Queen,
    HiveWorker,
    TestWorker,
)
from services import run_flow
from .roadmap import load_roadmap, save_roadmap, mark_task_done
import threading
import time


class AIController:
    """Orchestrate Queen and Hive Worker for a project."""

    def __init__(self, conn) -> None:
        self.conn = conn
        self.agents: Dict[str, BaseAgent] = {
            name: cls(conn, name) for name, cls in AGENT_REGISTRY.items()
        }
        self.queen = self.agents.get("queen")
        self.worker = self.agents.get("hive")
        self.tester = self.agents.get("tester")
        self._pause = threading.Event()
        self.running = False

    def run_project(self, project_id: int, idea: str, workspace: Path) -> None:
        """Plan tasks with Queen and execute them with a single worker."""
        self.running = True
        add_message(self.conn, project_id, "system", f"Starting project: {idea}")
        if self.queen:
            self.queen.plan_project(project_id, idea, workspace)
        for task in get_tasks(self.conn, project_id):
            while self._pause.is_set():
                time.sleep(0.1)
            update_task_status(self.conn, task["id"], "running")
            code = None
            if self.worker:
                code = self.worker.execute_task(
                    task["id"], project_id, task["description"], workspace
                )
            test_id = create_task(
                self.conn,
                project_id,
                "test",
                f"Tests for task {task['id']}",
                status="running",
            )
            status = "skipped"
            if self.tester and code is not None:
                status = self.tester.run_tests(project_id, task["id"], code)
            update_task_status(self.conn, test_id, status)
            try:
                row = get_project(self.conn, project_id)
                if row and row["roadmap"]:
                    path = Path(row["roadmap"])
                    data = load_roadmap(path)
                    mark_task_done(data, task["description"])
                    save_roadmap(data, path)
            except Exception:
                pass

        # run additional orchestration via Claude-Flow CLI
        try:
            output = run_flow(["npx", "claude-flow@alpha", "hive-mind", "wizard", "--force"])
            add_message(self.conn, project_id, "claude-flow", output)
        except Exception as exc:  # subprocess.CalledProcessError etc.
            add_message(self.conn, project_id, "error", str(exc))

        add_message(self.conn, project_id, "system", "All tasks completed")
        self.running = False

    # control helpers
    def pause(self) -> None:
        self._pause.set()

    def resume(self) -> None:
        self._pause.clear()

    def is_paused(self) -> bool:
        return self._pause.is_set()
