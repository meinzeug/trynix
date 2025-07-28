"""Simple text-to-speech helpers."""

from __future__ import annotations

try:  # optional dependency
    import pyttsx3
except Exception:  # pragma: no cover - optional
    pyttsx3 = None


def speak(text: str) -> None:
    """Read the given text aloud if pyttsx3 is available."""
    if pyttsx3 is None:  # pragma: no cover - optional
        return None
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

