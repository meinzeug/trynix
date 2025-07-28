"""PyInstaller build helper."""

from __future__ import annotations

import PyInstaller.__main__


def build() -> None:
    PyInstaller.__main__.run(
        [
            "--noconfirm",
            "--windowed",
            "--name=trynix",
            "main.py",
        ]
    )


if __name__ == "__main__":
    build()

