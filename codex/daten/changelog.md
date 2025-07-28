# Changelog

- 2024-06-06: Initiale Organisationsdateien erstellt (konzept, docs, milestones, brain, changelog, prompt).

- 2024-06-07: Milestone 1 umgesetzt: Grundstruktur, Basisklassen, DB-Init.

- 2025-07-28: Milestone 2 begonnen: GUI-Skelett mit Login und Dashboard implementiert.
- 2025-07-29: Chat- und Code-Viewer-Fenster hinzugefuegt. Dashboard startet sie fuer das ausgewaehlte Projekt.
- 2025-07-30: Milestone 3 gestartet: Services fuer OpenRouter und Claude-Flow, Agentengeruest und Taskfunktionen hinzugefuegt.
- 2025-07-31: AIController implementiert und ins Dashboard integriert.
- 2025-08-01: Claude-Flow-Integration im AIController, Dokumentation aktualisiert.
- 2025-08-01: STT-Modul und Mikrofon-Button im Chatfenster integriert.

- 2025-08-02: Automatisches Abhaken der Milestones implementiert.
- 2025-08-03: TestWorker fuehrt nach jeder Codegenerierung einen Syntaxcheck
  aus und protokolliert das Ergebnis. Milestone 4 Test-Tasks abgeschlossen.
- 2025-08-04: Live-Status-Anzeige fuer Agenten implementiert.
- 2025-08-05: Milestone 6 umgesetzt: Projekte sind nun Benutzern zugeordnet, das
  Rollen-/Rechtesystem (Admin/User) wurde integriert.
- 2025-08-06: Milestone 7 gestartet: Plugin-System, Darkmode-Plugin, TTS und
  PyInstaller-Build-Skript hinzugefuegt.
- 2025-08-07: LAN-Sharing implementiert: neuer Service `lan_share.py`, Share-Button im Dashboard, Dokumentation aktualisiert.
- 2025-08-08: Adminpanel und Settings-Fenster hinzugefuegt; Dokumentation ergaenzt.
- 2025-08-09: Milestone-Updater-Plugin hinzugefuegt. Aktualisiert Milestones automatisch beim Programmstart.
- 2025-08-09: Konzeptpruefung abgeschlossen. Fehlende Funktionen ermittelt und Milestones 8-11 angelegt (Live-Steuerung, Code-Highlighting, Queen-TTS, Agenten-Plugins).
- 2025-08-10: Milestone 8 begonnen: AIController pausierbar, Dashboard mit Pause/Resume-Buttons und Task-Manager.
- 2025-08-11: Milestone 9 umgesetzt: Code-Viewer mit Syntaxhighlighting und Einzeldatei-Export.
- 2025-08-12: Milestone 10 umgesetzt: automatische Queen-TTS mit einstellbarer Option im Settings-Fenster.
- 2025-08-13: Milestone 11 abgeschlossen: Agenten-Plugin-System um Beispiel-Plugin `custom_agent` erweitert.
- 2025-08-14: Milestone 12 umgesetzt: Projekt-Workspace mit Live-Dateibaum und ZIP-Export hinzugefügt.
- 2025-08-15: Milestone 13 umgesetzt: dynamische Roadmap mit GUI-Ansicht und Chat-Integration.
- 2025-08-16: Milestone 14 gestartet: Zauberstab-Feature und Feature Wizard hinzugefügt.
- 2025-08-17: Abschließende Tests durchgeführt und Refactoring des LAN-Sharing-Service.
- 2025-08-18: Konzeptpruefung: Adminrechte fuer Projekte und Settings fehlen. Milestone 15 eingetragen.

- 2025-08-19: Konzeptpruefung ergab fehlendes bcrypt-Hashing. Milestone 16 hinzugefuegt.
- 2025-08-20: Milestone 15 umgesetzt: Projektloeschung nur fuer Admins, Settings-Fenster ebenfalls eingeschraenkt.
- 2025-08-20: Milestone 16 gestartet: Passwort-Hashing mit bcrypt implementiert und Migration beim Login eingebaut.
- 2025-08-21: Milestone 16 abgeschlossen: Tests fuer Registrierung und Admin-Rechte ergaenzt, Dokumentation aktualisiert.
- 2025-08-22: Umsetzung und Tests von Milestone 15 und 16 verifiziert.
