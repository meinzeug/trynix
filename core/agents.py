from __future__ import annotations

from db import (
    create_task,
    update_task_status,
    add_code_file,
    add_message,
    set_project_roadmap,
)
from services.openrouter import send_prompt
import subprocess
import tempfile
from pathlib import Path

from speech import speak
from core.config import CONFIG
from .roadmap import save_roadmap
from typing import Dict, Type


class BaseAgent:
    def __init__(self, conn, name: str) -> None:
        self.conn = conn
        self.name = name


class Queen(BaseAgent):
    """Simple project planning agent."""

    def plan_project(self, project_id: int, idea: str, workspace: Path) -> None:
        response = send_prompt(
            f"Create a numbered task list for the following project idea:\n{idea}\nReturn one task per line."
        )
        add_message(self.conn, project_id, self.name, response)
        if CONFIG.tts_enabled:
            speak(response)
        tasks = []
        for line in response.splitlines():
            line = line.strip()
            if line:
                create_task(self.conn, project_id, "hive", line)
                tasks.append({"title": line, "status": "open"})

        roadmap = {
            "concept": idea,
            "milestones": [
                {"title": "Initial", "status": "open", "tasks": tasks}
            ],
        }
        path = workspace / "roadmap.json"
        save_roadmap(roadmap, path)
        set_project_roadmap(self.conn, project_id, str(path))


class HiveWorker(BaseAgent):
    """Basic code generation worker."""

    def execute_task(
        self, task_id: int, project_id: int, description: str, workspace: Path
    ) -> str:
        """Generate code for a task and return the code."""
        code = send_prompt(description)
        add_message(self.conn, project_id, self.name, code)
        rel_path = f"task_{task_id}.py"
        file_path = workspace / rel_path
        file_path.write_text(code, encoding="utf-8")
        add_code_file(self.conn, project_id, rel_path, code)
        update_task_status(self.conn, task_id, "done")
        return code


class TestWorker(BaseAgent):
    """Run simple syntax checks on generated code."""

    def run_tests(self, project_id: int, task_id: int, code: str) -> str:
        """Compile generated code to check for syntax errors."""
        tmp = tempfile.NamedTemporaryFile("w", suffix=".py", delete=False)
        try:
            tmp.write(code)
            tmp.close()
            result = subprocess.run(
                ["python", "-m", "py_compile", tmp.name],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                status = "passed"
                msg = "Syntax OK"
            else:
                status = "failed"
                msg = result.stderr.strip()
        finally:
            Path(tmp.name).unlink(missing_ok=True)

        add_message(
            self.conn,
            project_id,
            self.name,
            f"Test result for task {task_id}: {status}\n{msg}",
        )
        return status


# global registry for agent classes and their active state
AGENT_REGISTRY: Dict[str, Type[BaseAgent]] = {}
AGENT_ACTIVE: Dict[str, bool] = {}


def register_agent(name: str, cls: Type[BaseAgent]) -> None:
    """Register an agent class to be available for the controller."""

    AGENT_REGISTRY[name] = cls
    AGENT_ACTIVE.setdefault(name, True)


def activate_agent(name: str) -> None:
    """Enable an agent globally."""

    AGENT_ACTIVE[name] = True


def deactivate_agent(name: str) -> None:
    """Disable an agent globally."""

    AGENT_ACTIVE[name] = False


def is_agent_active(name: str) -> bool:
    """Return True if the agent is active."""

    return AGENT_ACTIVE.get(name, False)


# register built-in agents
register_agent("queen", Queen)
register_agent("hive", HiveWorker)
register_agent("tester", TestWorker)
