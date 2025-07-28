# Milestones fuer trynix

## Milestone 1: Projektgrundlage
- Repository initialisieren
- Grundlegende Verzeichnisstruktur (`gui/`, `core/`, `db/`, `services/`, `speech/`)
- Basisklassen fuer Konfiguration und Logging
- SQLite-Datenbank anlegen und Schema erzeugen

## Milestone 2: GUI-Skelett
- Einfache PySide6-Fensterstruktur (Login, Dashboard, Chat, Code-Viewer)
- Benutzer-Login und Registrierung implementieren
- Projektauswahl und -anlage

## Milestone 3: AI Core & Services
- Anbindung an OpenRouter (API-Key, Requests, Antwortverarbeitung)
- Integration der Claude-Flow CLI ueber `subprocess`
- Queen-Agent und Hive Worker als Grundgeruest implementieren
- Task-Verwaltung in der DB

## Milestone 4: Code-Generation & Testing
- Worker generieren Code-Files und speichern sie in `code_files`
- Test-Tasks anstoßen und Ergebnisse darstellen
- Chat-/Log-Ansicht mit allen Nachrichten (Tabelle `messages`)

## Milestone 5: Sprachsteuerung & erweiterte GUI
- STT-Modul fuer Spracheingabe integrieren
- Mikrofon-Button in der GUI
- Live-Status der Agenten anzeigen

## Milestone 6: Multi-Projekt und Benutzerrollen
- Mehrere Projekte parallel verwalten
- Rollen-/Rechtesystem (Admin, User)
- Sicheres API-Key-Handling und Passwort-Hashing

## Milestone 7: Deployment & Feinschliff
- Build mit PyInstaller fuer Windows und Linux
- Dokumentation erweitern
- Plugin-Schnittstelle vorbereiten
- Optionale Features (TTS, LAN-Sharing, Themes)

