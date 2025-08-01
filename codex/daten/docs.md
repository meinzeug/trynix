# Dokumentation fuer trynix

## Eingesetzte Technologien
- **Python 3.10+** als Programmiersprache
- **PySide6** fuer die GUI
- **SQLite** als lokale Datenbank
- **Node.js** >= 18 fuer die Nutzung der Claude-Flow CLI
- **Claude-Flow v2.0.0 Alpha** zur Orchestrierung der KI-Agenten
- **OpenRouter API** mit Modell `qwen/qwen3-coder:free`
- **speech_recognition** fuer Mikrofon-STT
- **PyInstaller** fuer das Packaging

## Moduluebersicht
- `main.py` startet die Anwendung und initialisiert die GUI
- `gui/` enthaelt die PySide6-Komponenten (Login, Dashboard, Code-Viewer, Chat)
- `core/` verwaltet das KI-Team (Queen, Hive Worker) und leitet Aufgaben an die Services weiter
- `db/` stellt Funktionen fuer den Zugriff auf die SQLite-Datenbank bereit
- `services/` kapselt die Anbindung zu OpenRouter und Claude-Flow
- `speech/` implementiert optionale Spracherkennung fuer Text-zu-Befehl
- `plugins/` enthaelt Erweiterungen wie den Darkmode
- `build.py` erstellt Installer

## API-Endpunkte und Prozesse
### OpenRouter
- HTTP-Aufrufe an `https://openrouter.ai/api/v1` mit dem Modell `qwen/qwen3-coder:free`
- Authentifizierung via API-Key (lokal gespeichert)
- Antworten liefern Text oder Code, der in `code_files` gespeichert wird

### Claude-Flow
- Lokale CLI-Aufrufe (z.B. `claude-flow@alpha hive-mind wizard --force`)
- Rueckgabedaten werden ueber `subprocess` gelesen und verarbeitet
- Der `AIController` startet nach der Codegenerierung automatisch einen Hive-Mind-Lauf und protokolliert die Ausgabe

## Ablaeufe
1. Benutzer meldet sich in der GUI an (Datenbank `users`)
2. Neues Projekt anlegen oder laden (`projects`)
3. Queen erstellt basierend auf der Projektidee Tasks und weist sie Hive Workern zu (`tasks`)
4. Hive Worker generieren Code ueber OpenRouter und testen ihn; Ergebnisse werden in `code_files` und `messages` gespeichert
5. GUI zeigt Chatverlauf und Code-Dateien an; der Benutzer kann eingreifen oder fortfahren
6. Claude-Flow orchestriert parallele Agentenlaeufe und wird dabei vom Core angesteuert

## Besonderheiten
- Alle Daten bleiben lokal; keine Cloudspeicherung
- API-Schluessel werden in einer Datei gesichert und niemals in den Code eingebettet
- Passwoerter werden beim Speichern gehasht
- Passwort-Hashing erfolgt mit `bcrypt`; alte SHA256-Hashes werden beim Login automatisch migriert
- Plugin-System ermoeglicht Erweiterungen (z.B. neue Agenten oder Funktionen)
- TTS-Ausgabe fuer Rueckmeldungen der Queen
- Beispiel-Plugin aktiviert Darkmode in der GUI
- Beispiel-Plugin fuer einen Echo-Agent demonstriert die Agenten-Schnittstelle
- `build.py` baut Windows- und Linux-Installer via PyInstaller
- `lan_share.py` ermoeglicht Projekt-Sharing ueber einen lokalen HTTP-Server
- Adminpanel und Settings-Fenster sind in der GUI integriert
- Nur Admins koennen Projekte loeschen und die Einstellungen oeffnen

## Erweiterte Live-Steuerung
- KI-Laeufe lassen sich im Dashboard pausieren und fortsetzen.
- Tasks koennen manuell bearbeitet oder neu angelegt werden.
- Eine Statusanzeige zeigt "Running" oder "Paused" an.

## Projekt-Workspace & ZIP-Export
- Alle generierten Dateien liegen in einem zentralen Ordner `workspace/`.
- Jeder KI-Lauf legt darunter einen Unterordner mit `<projektname-timestamp>` an.
- Die GUI zeigt den Ordner mit `QFileSystemModel` live an und aktualisiert sich bei Änderungen.
- Beim Anklicken einer Datei öffnet sich ein schreibgeschützter Editor mit Syntaxhighlighting.
- Über einen Export-Button wird der Projektordner mit `shutil.make_archive` als ZIP gepackt und kann gespeichert werden.
- Der Pfad zum jeweils aktiven Workspace wird in der Tabelle `projects` gespeichert.
- `QFileSystemModel` überwacht das Verzeichnis und meldet Änderungen über `directoryChanged`-Signale.

## Dynamische Roadmap & Queen-Dialog
- Nach der Projektanlage erzeugt die Queen automatisch ein Konzept und eine detaillierte Roadmap.
- Diese Roadmap wird als `roadmap.json` im jeweiligen Projektordner gespeichert und in der Tabelle `projects` verlinkt.
- Sie enthält Meilensteine und Unteraufgaben mit den Stati `open`, `in_progress` und `done`.
- Änderungen durch die Queen aktualisieren sowohl die JSON-Datei als auch die Datenbank.
- In der GUI erscheint eine eigene Ansicht (z. B. Sidebar mit `QTreeView`), die den aktuellen Stand der Roadmap live anzeigt.
- Nutzer können per Chat oder Spracheingabe Änderungswünsche einreichen; nach Bestätigung passt die Queen die Roadmap an und speichert sie erneut.

## Zauberstab - automatische Feature-Innovation
- In der GUI erscheint ein 🪄-Icon mit Tooltip "Lass die Queen neue Features vorschlagen".
- Beim Klick analysiert die Queen die aktuelle Codebasis im Ordner `workspace/` und liest `milestones.md`.
- Aus diesen Informationen entwickelt sie 2–5 kreative Funktionsideen mit kurzer Beschreibung und Nutzenargumentation.
- Die Ideen erscheinen im "Feature Wizard"-Fenster und können einzeln über den Button "Zur Roadmap hinzufügen" übernommen werden.
- Akzeptierte Vorschläge werden als neuer Milestone samt Subtasks an `milestones.md` angehängt und optional als Notiz in `brain.md` vermerkt.
- Der gesamte Ablauf wird im Chat und den Logs dokumentiert und lässt sich später nachvollziehen.

## Eigene Agenten & Tools
Neue Agenten werden als Python-Klassen definiert, die `BaseAgent` erweitern. Eine YAML-Datei `agents.yaml` speichert Name, Beschreibung, Spezialisierung und optionale Fähigkeiten. Beim Start lädt ein Plugin diese Datei, erzeugt entsprechende Agentenklassen und meldet sie über `register_agent()` im System an.

Tools sind ebenfalls per YAML konfigurierbar. Jede Definition enthält `name`, `description`, `command` und optionale Eingabeparameter. Ein Tool-Editor im Adminbereich schreibt neue Einträge in `tools.yaml` und registriert sie beim Start automatisch. Über dieselbe Schnittstelle lassen sich Einträge bei Bedarf auch wieder entfernen. Die Agentenkonfiguration legt fest, welche Tools ein Agent verwenden darf. Beim Laden prüft das Plugin, ob alle genannten Tools existieren und ordnet sie den Agenten zu.

Die Queen lädt alle über Plugins registrierten Agenten automatisch und stellt sie dem Controller bereit. Über das Dashboard lassen sich Agenten bei Bedarf deaktivieren.


## Zentrale Kontext-Engine
Die Anwendung verwaltet alle relevanten Zustände in einer globalen Kontextstruktur (`context_state.json`). Diese besteht aus:

- `history` – vollständige Gesprächsverläufe
- `agents` – aktueller Status der einzelnen Agenten
- `task_flow` – sämtliche Routinen mit Bearbeitungsstatus
- `handoffs` – protokollierte Übergaben inkl. Kontext
- `user_actions` – manuelle Eingriffe und Entscheidungen des Nutzers

Die Struktur wird bei jedem Ereignis automatisch fortgeschrieben und lässt sich über eine API lesen oder aktualisieren. Optional können die Daten zusätzlich in der Datenbank gesichert werden.
Ein kleines Fenster in der GUI zeigt den Inhalt von `context_state.json` live an.
