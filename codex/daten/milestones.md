# Milestones fuer trynix

## Milestone 1: Projektgrundlage
- [x] Repository initialisieren
- [x] Grundlegende Verzeichnisstruktur (`gui/`, `core/`, `db/`, `services/`, `speech/`)
- [x] Basisklassen fuer Konfiguration und Logging
- [x] SQLite-Datenbank anlegen und Schema erzeugen

## Milestone 2: GUI-Skelett
- [x] Einfache PySide6-Fensterstruktur (Login, Dashboard, Chat, Code-Viewer)
- [x] Benutzer-Login und Registrierung implementieren
- [x] Projektauswahl und -anlage

## Milestone 3: AI Core & Services
- [x] Anbindung an OpenRouter (API-Key, Requests, Antwortverarbeitung)
- [x] Integration der Claude-Flow CLI ueber `subprocess`
- [x] Queen-Agent und Hive Worker als Grundgeruest implementieren
- [x] Task-Verwaltung in der DB

## Milestone 4: Code-Generation & Testing
- [x] Worker generieren Code-Files und speichern sie in `code_files`
- [x] Test-Tasks anstoßen und Ergebnisse darstellen
- [x] Chat-/Log-Ansicht mit allen Nachrichten (Tabelle `messages`)

## Milestone 5: Sprachsteuerung & erweiterte GUI
- [x] STT-Modul fuer Spracheingabe integrieren
- [x] Mikrofon-Button in der GUI
- [x] Live-Status der Agenten anzeigen

## Milestone 6: Multi-Projekt und Benutzerrollen
- [x] Mehrere Projekte parallel verwalten
- [x] Rollen-/Rechtesystem (Admin, User)
- [x] Sicheres API-Key-Handling und Passwort-Hashing

## Milestone 7: Deployment & Feinschliff
- [x] Build mit PyInstaller fuer Windows und Linux
- [x] Dokumentation erweitern
- [x] Plugin-Schnittstelle vorbereiten
- [x] Optionale Features (TTS, LAN-Sharing, Themes)


## Milestone 8: Erweiterte Live-Steuerung
- [ ] KI-Ausfuehrung im Dashboard pausieren und fortsetzen koennen
- [ ] Tasks manuell bearbeiten oder neue hinzufuegen
- [ ] UI-Statusanzeige fuer laufende/pausierte Prozesse
- [ ] AIController um Pausen-Logik erweitern

## Milestone 9: Verbesserter Code-Viewer
- [ ] Syntaxhighlighting fuer Python-Code implementieren
- [ ] Option zum Speichern einzelner Dateien

## Milestone 10: Automatische Queen-TTS
- [ ] Queen-Nachrichten automatisch ueber TTS ausgeben
- [ ] Schalter in den Einstellungen zum Aktivieren/Deaktivieren

## Milestone 11: Agenten-Plugin-System
- [ ] Plugin-Schnittstelle erweitern, um neue Agenten einzubinden
- [ ] Beispielplugin fuer einen Custom-Agent bereitstellen
