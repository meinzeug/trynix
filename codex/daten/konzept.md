# Konzept fuer trynix

## Ziel
trynix ist eine plattformuebergreifende Desktop-Anwendung, die ein KI-basiertes
Entwicklungsteam orchestriert. Benutzer geben lediglich ihre Projektidee ein und
werden durch eine Projektleiterin-KI ("Queen") angeleitet. Spezialisierte
"Hive Worker"-Agenten uebernehmen Planung, Codierung und Testing. Der komplette
Ablauf laeuft lokal und wird in Echtzeit ueber eine moderne GUI gesteuert.

## Funktionen
- KI-gesteuerte Projektleitung mit automatischer Aufgabenverteilung
- Schwarmintelligenz aus spezialisierten Agenten fuer Planung, Code und Tests
- Live-Steuerung ueber eine PySide6-GUI (pausieren, fortsetzen, eingreifen)
- Multi-Projekt- und Multi-User-Unterstuetzung mit Benutzerverwaltung
- Persistente Speicherung aller Daten in einer lokalen SQLite-Datenbank
- Integration des Modells `qwen/qwen3-coder:free` via OpenRouter
- Orchestrierung der KI-Agenten durch Claude-Flow CLI
- Optional Sprachsteuerung per STT
- Code-Browser fuer alle generierten Dateien
- Export und Deployment mit PyInstaller

## Struktur und Komponenten
- **main.py** – Einstiegspunkt der Anwendung
- **gui/** – PySide6-Komponenten: Login, Dashboard, Chat/Log, Code-Viewer
- **core/** – zentrale Logik, AI-Controller, Agent-Management
- **db/** – Initialisierung und Zugriff auf SQLite
- **services/** – Schnittstellen zu OpenRouter und Claude-Flow
- **speech/** – Sprachsteuerung via STT
- **.trynix/** – Projekt- und Log-Daten

### Datenbankdesign
- `users` – Benutzername, Passwort-Hash, Rolle
- `projects` – Projekte, Beschreibung, Status
- `code_files` – erzeugte Dateien inkl. Projektzuordnung
- `tasks` – KI-Tasks mit zustaendigem Agent und Status
- `messages` – Kommunikation mit der Queen

## Besonderheiten
- Lokale Ausfuehrung ohne Cloud-Backend
- Sicherheit durch Passwort-Hashing und lokale API-Key-Verwaltung
- Erweiterbarkeit durch geplantes Plugin-System
- Geplante Features: TTS-Ausgabe, Projekt-Sharing im LAN, Themes/Darkmode
