"""Speech helpers for trynix."""

from __future__ import annotations

try:  # optional dependency
    import speech_recognition as sr
except Exception:  # pragma: no cover - optional
    sr = None

try:  # optional dependency
    from .tts import speak
except Exception:  # pragma: no cover - optional
    def speak(text: str) -> None:
        """Fallback speak when pyttsx3 is unavailable."""
        return None


def transcribe_from_microphone(timeout: int = 5) -> str:
    """Record audio from the default microphone and return the transcript.

    Parameters
    ----------
    timeout:
        Maximum length in seconds for a single utterance.
    """

    if sr is None:  # pragma: no cover - optional
        return ""

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source, phrase_time_limit=timeout)
    return recognizer.recognize_google(audio)

__all__ = ["transcribe_from_microphone", "speak"]
