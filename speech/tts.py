"""Simple text-to-speech helpers."""

from __future__ import annotations

import pyttsx3


def speak(text: str) -> None:
    """Read the given text aloud."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

