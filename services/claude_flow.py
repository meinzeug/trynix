from __future__ import annotations

import subprocess
from typing import Iterable


def run_flow(args: Iterable[str]) -> str:
    """Run the Claude-Flow CLI and return its stdout."""
    result = subprocess.run(list(args), capture_output=True, text=True, check=True)
    return result.stdout
