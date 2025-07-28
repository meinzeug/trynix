from __future__ import annotations

from db import (
    create_task,
    update_task_status,
    add_code_file,
    add_message,
)
from services.openrouter import send_prompt


class BaseAgent:
    def __init__(self, conn, name: str) -> None:
        self.conn = conn
        self.name = name


class Queen(BaseAgent):
    """Simple project planning agent."""

    def plan_project(self, project_id: int, idea: str) -> None:
        response = send_prompt(
            f"Create a numbered task list for the following project idea:\n{idea}\nReturn one task per line."
        )
        add_message(self.conn, project_id, self.name, response)
        for line in response.splitlines():
            line = line.strip()
            if line:
                create_task(self.conn, project_id, "hive", line)


class HiveWorker(BaseAgent):
    """Basic code generation worker."""

    def execute_task(self, task_id: int, project_id: int, description: str) -> None:
        code = send_prompt(description)
        add_message(self.conn, project_id, self.name, code)
        file_path = f"task_{task_id}.py"
        add_code_file(self.conn, project_id, file_path, code)
        update_task_status(self.conn, task_id, "done")
