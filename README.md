# 🧠 trynix – KI-Schwarmintelligenz für automatisierte Softwareentwicklung

**trynix** ist eine plattformübergreifende Desktop-Anwendung zur vollständigen KI-gesteuerten Softwareentwicklung – orchestriert durch Schwarmintelligenz, visuell gesteuert über eine moderne GUI mit **PySide6**, angetrieben von **OpenRouter** (mit dem Modell `qwen/qwen3-coder:free`) und orchestriert durch **Claude-Flow v2.0.0 Alpha**.  
Die Software führt ein ganzes KI-Entwicklungsteam – eine Projektleiterin-KI (*Queen*) delegiert spezialisierte Agenten (*Hive Worker*) und entwickelt so vollständig automatisch lauffähige Software. Der Nutzer beobachtet, beeinflusst und steuert den gesamten Ablauf in Echtzeit.

---

## 🚀 Hauptfeatures

- **KI-gesteuerte Projektleitung**: Nur Idee eingeben – der Rest läuft automatisch.
- **Hive-Mind mit Schwarm-Agents**: Planung, Codierung, Testing, alles KI-gesteuert.
- **Live-Steuerung in der GUI**: Eingreifen, pausieren, fortsetzen oder Aufgaben manuell ändern.
- **Multi-Projekt & Multi-User**: Benutzerverwaltung, Rollen, Projekte separat verwaltbar.
- **Persistente Speicherstruktur**: Lokale SQLite-DB zur Protokollierung und Wiederaufnahme.
- **Modell: `qwen/qwen3-coder:free`** über OpenRouter – kostenlos & extrem leistungsfähig.
- **Claude-Flow Orchestrierung**: Nutzung der Hive-/Swarm-Architektur für verteilte Agentenarbeit.
- **Sprachsteuerung (optional)**: Eingabe auch per Mikrofon mit STT.
- **Code-Browser & Export**: Alle generierten Dateien einsehbar und exportierbar.
- **Plattformübergreifend**: Läuft auf Windows & Linux als PySide6 Desktop-App.

---

## 🧬 Architekturübersicht

```mermaid
graph TD
    GUI[PySide6 GUI]
    Login[Login/Benutzer]
    Dashboard[Projekt-Dashboard]
    Chat[Chat + Mikrofon]
    Code[Code-Viewer]

    Core[AI Controller (Python)]
    DB[(SQLite DB)]
    ClaudeFlow[Claude-Flow CLI]
    OpenRouter[OpenRouter API (Qwen3-Coder)]

    GUI --> Login
    GUI --> Dashboard
    GUI --> Chat
    GUI --> Code

    Dashboard --> Core
    Chat --> Core
    Code --> Core
    Login --> DB
    Dashboard --> DB

    Core --> ClaudeFlow
    Core --> OpenRouter
    Core --> DB
```

---

## 📁 Modulstruktur

| Modul             | Beschreibung |
|-------------------|--------------|
| `main.py`         | Startpunkt der App |
| `gui/`            | PySide6-Komponenten (Login, Dashboard, CodeViewer etc.) |
| `core/`           | AI-Kontroller, Projektlogik, Agent-Management |
| `db/`             | SQLite-Init & Zugriff |
| `services/`       | Schnittstellen zu OpenRouter & Claude-Flow |
| `speech/`         | STT-Integration für Spracheingabe |
| `.trynix/`        | Projektdaten, Memory, Logfiles, Ergebnisse |

---

## 🧠 Claude-Flow Integration

Claude-Flow wird über Node.js lokal installiert und von `trynix` via CLI gesteuert:

```bash
npm install -g @anthropic-ai/claude-code
npx claude-flow@alpha init
```

Beispielhafter Hive-Mind-Start:
```bash
npx claude-flow@alpha hive-mind wizard --force
```

trynix ruft diese Prozesse intern über `subprocess` auf und parst die Rückgaben. Memory und Logs werden automatisch ins Projekt eingebunden.

---

## 🧠 KI-Modelle via OpenRouter

Das Hauptmodell ist:

```
qwen/qwen3-coder:free
```

Dieses Modell wird über die [OpenRouter API](https://openrouter.ai/) angesteuert.  
trynix unterstützt beliebige OpenRouter-kompatible Modelle. Der Key wird in der GUI unter „Einstellungen“ eingetragen.

---

## 🗂 Datenbankdesign (SQLite)

| Tabelle         | Inhalt |
|------------------|--------|
| `users`          | Username, Passwort (gehasht), Rolle |
| `projects`       | Projektname, Beschreibung, Status |
| `code_files`     | Datei-Inhalte, Zugehörigkeit zum Projekt |
| `tasks`          | KI-Tasks, Zuständiger Agent, Status |
| `messages`       | Verlauf aus Chat / Kommunikation mit Queen |

Die Datenbank wird bei Erststart automatisch erzeugt.

---

## 💻 GUI-Komponenten

- **Login/Registrierung**
- **Projektübersicht + Projektwechsel**
- **Live-KI-Log (Chat + Statusmeldungen)**
- **Task-Panel mit Agentenzuordnung**
- **Code-Viewer mit Syntaxhighlighting**
- **Mikrofonbutton für Spracheingabe**
- **Adminpanel zur Benutzerverwaltung**

---

## 🔐 Sicherheit

- Lokale Speicherung (keine Cloud)
- Passwort-Hashing (z. B. bcrypt)
- API-Key-Handling sicher in Datei
- Nur Admin darf Projekte löschen, Konfiguration ändern

---

## 📦 Deployment & Installation

### Voraussetzungen

- Python 3.10+
- Node.js ≥ 18
- Claude-Flow CLI installiert
- OpenRouter API-Key

### Build mit PyInstaller

```bash
pyinstaller --noconfirm --windowed --name trynix main.py
```

Installer-Pakete für Windows/Linux können generiert und veröffentlicht werden.

---

## 📈 Geplante Features

- [ ] TTS für Sprachausgabe der Queen
- [ ] Projekt-Sharing über LAN
- [ ] Themes/Darkmode
- [ ] Plugin-System für eigene Agenten

---

## 🧠 Vision

**trynix** ist der nächste Schritt zu *AI-Native Softwareentwicklung*:  
Statt Tools zu benutzen, gibst du deiner Idee Raum – und ein Schwarm künstlicher Agenten erschafft daraus funktionierende Software. Inklusive Feedback, Kontrolle und interaktiver Iteration.

---

## 👑 Lizenz

MIT – Open Source. Entwickelt mit Herz, Qwen und Schwarmintelligenz.

---

## 📫 Mitmachen?

Wenn du helfen willst, trynix weiterzuentwickeln:
→ Forke, erstelle Issues, oder kontaktiere [Dennis](https://github.com/meinzeug)

