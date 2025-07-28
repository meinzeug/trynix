"""Speech helpers for trynix."""

from __future__ import annotations

import speech_recognition as sr
from .tts import speak


def transcribe_from_microphone(timeout: int = 5) -> str:
    """Record audio from the default microphone and return the transcript.

    Parameters
    ----------
    timeout:
        Maximum length in seconds for a single utterance.
    """

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source, phrase_time_limit=timeout)
    return recognizer.recognize_google(audio)

__all__ = ["transcribe_from_microphone", "speak"]
