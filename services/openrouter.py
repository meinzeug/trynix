from __future__ import annotations

from pathlib import Path
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "qwen/qwen3-coder:free"


def load_api_key(path: Path = Path('.openrouter_key')) -> str:
    """Return the stored OpenRouter API key."""
    return Path(path).read_text().strip()


def save_api_key(key: str, path: Path = Path('.openrouter_key')) -> None:
    """Save the OpenRouter API key to the given path."""
    Path(path).write_text(key.strip())


def send_prompt(prompt: str, *, model: str = DEFAULT_MODEL, key_path: Path | str = '.openrouter_key') -> str:
    """Send a prompt to the OpenRouter API and return the text response."""
    api_key = load_api_key(Path(key_path))
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]
