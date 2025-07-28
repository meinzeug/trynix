import re
from pathlib import Path

DONE_PREFIXES = {
    "Repository initialisieren": True,
    "Grundlegende Verzeichnisstruktur": True,
    "Basisklassen fuer Konfiguration und Logging": True,
    "SQLite-Datenbank anlegen": True,
    "Einfache PySide6-Fensterstruktur": True,
    "Benutzer-Login und Registrierung": True,
    "Projektauswahl und -anlage": True,
    "Anbindung an OpenRouter": True,
    "Integration der Claude-Flow CLI": True,
    "Queen-Agent und Hive Worker": True,
    "Task-Verwaltung": True,
    "Worker generieren Code-Files": True,
    "Test-Tasks": False,
    "Chat-/Log-Ansicht": True,
    "STT-Modul": True,
    "Mikrofon-Button": True,
    "Live-Status": False,
    "Mehrere Projekte parallel": False,
    "Rollen-/Rechtesystem": False,
    "Sicheres API-Key-Handling": True,
    "Build mit PyInstaller": False,
    "Dokumentation erweitern": False,
    "Plugin-Schnittstelle": False,
    "Optionale Features": False,
}

CHECKBOX_RE = re.compile(r'^(\s*-)(?:\s*\[[ xX]\])?\s*(.*)$')


def update_line(line: str) -> str:
    m = CHECKBOX_RE.match(line)
    if not m:
        return line
    bullet = m.group(2)
    done = False
    for prefix, status in DONE_PREFIXES.items():
        if bullet.startswith(prefix):
            done = status
            break
    box = '[x]' if done else '[ ]'
    return f"{m.group(1)} {box} {bullet}"


def update_file(path: Path) -> None:
    lines = path.read_text(encoding='utf-8').splitlines()
    updated = [update_line(line) for line in lines]
    path.write_text("\n".join(updated) + "\n", encoding='utf-8')


if __name__ == '__main__':
    update_file(Path('codex/daten/milestones.md'))
