# Dokumentation fuer trynix

## Eingesetzte Technologien
- **Python 3.10+** als Programmiersprache
- **PySide6** fuer die GUI
- **SQLite** als lokale Datenbank
- **Node.js** >= 18 fuer die Nutzung der Claude-Flow CLI
- **Claude-Flow v2.0.0 Alpha** zur Orchestrierung der KI-Agenten
- **OpenRouter API** mit Modell `qwen/qwen3-coder:free`
- **PyInstaller** fuer das Packaging

## Moduluebersicht
- `main.py` startet die Anwendung und initialisiert die GUI
- `gui/` enthaelt die PySide6-Komponenten (Login, Dashboard, Code-Viewer, Chat)
- `core/` verwaltet das KI-Team (Queen, Hive Worker) und leitet Aufgaben an die Services weiter
- `db/` stellt Funktionen fuer den Zugriff auf die SQLite-Datenbank bereit
- `services/` kapselt die Anbindung zu OpenRouter und Claude-Flow
- `speech/` implementiert optionale Spracherkennung fuer Text-zu-Befehl

## API-Endpunkte und Prozesse
### OpenRouter
- HTTP-Aufrufe an `https://openrouter.ai/api/v1` mit dem Modell `qwen/qwen3-coder:free`
- Authentifizierung via API-Key (lokal gespeichert)
- Antworten liefern Text oder Code, der in `code_files` gespeichert wird

### Claude-Flow
- Lokale CLI-Aufrufe (z.B. `claude-flow@alpha hive-mind wizard --force`)
- Rueckgabedaten werden ueber `subprocess` gelesen und verarbeitet

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
- Geplantes Plugin-System ermoeglicht Erweiterungen (z.B. neue Agenten oder Funktionen)
