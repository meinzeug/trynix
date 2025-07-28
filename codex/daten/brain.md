# Brain

- Startpunkt des Projekts. Noch keine Codebasis vorhanden.
- Naechster Schritt: Implementierung gemaess Milestone 1.
- Milestone 1 umgesetzt: Verzeichnisstruktur angelegt, Config/Logging-Module und DB-Init implementiert.
- Milestone 2 begonnen: Einfaches GUI-Skelett mit Login und Dashboard erstellt. Benutzer koennen sich registrieren und einloggen, Projekte lassen sich anlegen.
- Milestone 2 erweitert: Chatfenster und Code-Viewer als einfache Widgets umgesetzt. Dashboard oeffnet sie projektbezogen.
- Milestone 3 begonnen: OpenRouter- und Claude-Flow-Services sowie Agenten-Grundklassen implementiert.
- Milestone 3 fortgefuehrt: AIController zum Orchestrieren von Queen und Hive hinzugefuegt. Dashboard startet nun die KI fuer ein Projekt.
- Milestone 5 begonnen: STT-Modul mit Mikrofon-Button im Chat implementiert.
- Claude-Flow-Integration erweitert: AIController startet nach der Codegenerierung einen Hive-Mind-Lauf und schreibt die Ausgabe ins Nachrichtenlog.

- Automatisches Update-Skript fuer Milestones erstellt und ausgefuehrt.
- TestWorker implementiert: Fuehrt Syntaxchecks nach jeder Codegenerierung aus
  und schreibt das Ergebnis ins Chatlog. Milestone 4 "Test-Tasks" damit
  abgeschlossen.
- Live-Status-Anzeige fuer Agenten im Dashboard umgesetzt.
- Multi-Projekt-Verwaltung eingefuehrt: Projekte speichern nun den Besitzer und
  das Dashboard zeigt je nach Rolle nur eigene oder alle Projekte an.
- Rollen-/Rechtesystem implementiert (Admin/User) und Login gibt Rolle sowie
  User-ID zurueck.
- Plugin-System vorbereitet: Plugins koennen sich bei Start registrieren.
- Beispiel-Darkmode-Plugin erstellt und per Loader eingebunden.
- TTS-Unterstuetzung fuer Chatnachrichten implementiert.
- Build-Skript fuer PyInstaller hinzugefuegt.
- LAN-Sharing umgesetzt: neuer Service zum Teilen eines Projekts als ZIP per HTTP und Share-Button im Dashboard.
- Adminpanel und Settings-Fenster fuer API-Key implementiert.
- Milestone-Updater-Plugin erstellt: aktualisiert milestones.md beim Start.
- Konzeptpruefung: Anforderungen mit README abgeglichen. Folgende Funktionen fehlen:
  - Pausieren/Fortsetzen der KI-Laeufe und manuelle Taskbearbeitung
  - Syntaxhighlighting im Code-Viewer
  - Automatische TTS-Ausgabe fuer Queen-Meldungen
  - Erweiterbare Agenten via Plugin-Schnittstelle
- Neue Milestones 8 bis 11 entsprechend angelegt.
- Milestone 8 gestartet: Dashboard erhielt Pause/Resume und Task-Manager, AIController verfuegt nun ueber Pausenlogik.
- Milestone 9 abgeschlossen: Python-Code wird im Code-Viewer farbig hervorgehoben und einzelne Dateien koennen gespeichert werden.
- Milestone 10 umgesetzt: Queen-Nachrichten werden bei aktivierter Einstellung automatisch per TTS vorgelesen. Settings-Fenster bietet nun Checkbox zur Steuerung.
- Milestone 11 gestartet und abgeschlossen: Beispiel-Plugin `custom_agent` registriert einen Echo-Agenten über die Plugin-Schnittstelle.
- Milestone 12 umgesetzt: Workspace-Verzeichnis pro Projektlauf mit Live-Dateibaum und ZIP-Export implementiert.
- Milestone 13 umgesetzt: Queen erstellt Roadmap, GUI zeigt Fortschritt und Chat kann Änderungen übernehmen.
- Milestone 14 begonnen: Zauberstab-Funktion implementiert, Feature Wizard erstellt.
- Konzeptabgleich 2025-08-18: README verlangt Admin-Rechte fuer Projektloeschung und Konfiguration. Funktion fehlt. Milestone 15 angelegt.

- Konzeptabgleich 2025-08-19: README fordert bcrypt-Hashing. Muss noch umgesetzt werden (Milestone 16).
- Milestone 15 umgesetzt: Projekte lassen sich nun durch Admins löschen und das Settings-Fenster ist nur noch für Admins sichtbar.
- Milestone 16 abgeschlossen: Passwort-Hashing verwendet bcrypt; Altdaten werden beim ersten Login migriert und neue Tests pruefen Admin-Berechtigungen.
- Milestone 17 umgesetzt: Neuer Dialog zum Anlegen von Agenten, YAML-Speicherung
  und Plugin zum Laden der definierten Agenten. Tests decken Speicherung und
  Registrierung ab.
 - Milestone 18 umgesetzt: Tool-Editor erstellt, Tools werden persistent in
   `tools.yaml` gespeichert und beim Start registriert. Der Agenten-Dialog zeigt
   verfügbare Tools zur Auswahl und Tests prüfen Registrierung und Zuordnung.
   Beim Laden von YAML-Agenten wird nun geprüft, ob alle referenzierten Tools existieren.
- Milestone 19 umgesetzt: Controller lädt alle registrierten Agenten dynamisch,
  Dashboard bietet einen Dialog zum Aktivieren oder Deaktivieren.
- Milestone 20 abgeschlossen: Zentrale Kontext-Engine speichert alle
  Zustände in `context_state.json`, kann optional in der DB gesichert werden
  und ist über ein eigenes GUI-Fenster einsehbar.
