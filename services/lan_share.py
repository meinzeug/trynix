from __future__ import annotations

from http.server import HTTPServer, SimpleHTTPRequestHandler
from tempfile import TemporaryDirectory
from threading import Thread
from pathlib import Path
import zipfile
from typing import Tuple

from db import get_code_files


def start_share(conn, project_id: int, host: str = "0.0.0.0", port: int = 8000) -> Tuple[HTTPServer, Thread, TemporaryDirectory, str]:
    """Start a simple HTTP server to share project files as a ZIP archive.

    Returns ``(server, thread, tempdir, url)``. The caller must keep the returned
    ``TemporaryDirectory`` alive while the server is running and call
    :func:`stop_share` afterwards.
    """
    tmpdir = TemporaryDirectory()
    zip_path = Path(tmpdir.name) / f"project_{project_id}.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        for row in get_code_files(conn, project_id):
            zf.writestr(row["path"], row["content"] or "")

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, directory: str = tmpdir.name, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

    httpd = HTTPServer((host, port), Handler)
    thread = Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    url = f"http://{host}:{port}/{zip_path.name}"
    return httpd, thread, tmpdir, url


def stop_share(server: HTTPServer, thread: Thread, tmpdir: TemporaryDirectory) -> None:
    """Stop the running share server and clean up temporary files."""
    server.shutdown()
    thread.join()
    tmpdir.cleanup()
