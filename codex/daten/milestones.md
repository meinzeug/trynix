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
- [x] KI-Ausfuehrung im Dashboard pausieren und fortsetzen koennen
- [x] Tasks manuell bearbeiten oder neue hinzufuegen
- [x] UI-Statusanzeige fuer laufende/pausierte Prozesse
- [x] AIController um Pausen-Logik erweitern

## Milestone 9: Verbesserter Code-Viewer
- [x] Syntaxhighlighting fuer Python-Code implementieren
- [x] Option zum Speichern einzelner Dateien

## Milestone 10: Automatische Queen-TTS
- [x] Queen-Nachrichten automatisch ueber TTS ausgeben
- [x] Schalter in den Einstellungen zum Aktivieren/Deaktivieren

## Milestone 11: Agenten-Plugin-System
- [x] Plugin-Schnittstelle erweitern, um neue Agenten einzubinden
- [x] Beispielplugin fuer einen Custom-Agent bereitstellen

## Milestone 12: Live-Projekt-Workspace & ZIP-Export
 - [x] Zentrales Verzeichnis `workspace/` anlegen
 - [x] Unterordner `<projektname-timestamp>` bei jedem Agentenlauf erstellen
 - [x] Dateibaum in der GUI mit `QFileSystemModel` live anzeigen
 - [x] Dateien per Klick in schreibgeschütztem Editor mit Syntaxhighlighting öffnen
 - [x] Änderungen am Workspace in Echtzeit verfolgen
 - [x] Projektordner über einen Button als ZIP exportieren
 - [x] Archivierung mit `shutil.make_archive` implementieren
 - [x] Pfadverwaltung und DB-Eintrag für den Workspace ergänzen

## Milestone 13: Dynamische Roadmap & Queen-Dialog
- [x] Queen erzeugt aus der Nutzeridee automatisch ein vollständiges Konzept
  (Funktionsübersicht, Struktur und Technologieeinsatz).
- [x] Generierte Roadmap mit Meilensteinen und Subtasks dauerhaft speichern
  (JSON-Datei und DB-Eintrag).
- [x] GUI zeigt eine Live-Roadmap-Ansicht mit Status (offen/in Arbeit/erledigt).
- [x] Queen überwacht die Roadmap und markiert erledigte Punkte automatisch.
- [x] Änderungswünsche lassen sich über Chat oder Spracheingabe einreichen.
- [x] Nach Bestätigung durch die Queen wird die Roadmap angepasst und erneut
  gespeichert.

## Milestone 14: Zauberstab - automatische Feature-Innovation
- [x] Zauberstab-Icon (🪄) in der GUI mit Tooltip "Lass die Queen neue Features vorschlagen"
- [x] Klick analysiert Codebasis unter `workspace/` sowie `milestones.md`
- [x] Queen entwickelt daraus 2–5 neue Feature-Ideen inkl. Nutzenbeschreibung
- [x] Ideen erscheinen in einem Panel mit Button "Zur Roadmap hinzufügen"
- [x] Akzeptierte Vorschläge werden als neuer Milestone mit Subtasks in `milestones.md` eingetragen
- [x] Optional Notizen zu den Features in `brain.md` speichern
- [x] Ergebnis und Aktionen im Chat/Log dokumentieren
- [x] Tests und Dokumentation der Funktion anlegen


## Milestone 15: Admin-Rechte fuer Projekte und Konfiguration
- [x] Funktion `delete_project` im Modul `db` implementieren
- [x] Loeschoption im Dashboard integrieren; Button nur fuer Admin sichtbar
- [x] Zugriff auf das Settings-Fenster auf Admins beschraenken
- [x] Tests fuer Projektloeschung und Berechtigungen erstellen
- [x] Dokumentation und brain.md um neue Admin-Features ergaenzen

## Milestone 16: Sichere Passwort-Hashes mit bcrypt
- [x] Bibliothek `bcrypt` als Abhängigkeit einbinden
- [x] Passwort-Hashing bei Registrierung auf bcrypt umstellen
- [x] Existierende Passwörter beim ersten Login migrieren
- [x] Authentifizierung mit bcrypt-Hashes prüfen
- [x] Tests für Registrierung, Login und Migration ergänzen
- [x] Dokumentation und changelog aktualisieren

## Milestone 17: Agenten-Erstellung
- [x] Dialog "Agent anlegen" in der GUI bereitstellen
- [x] Backend-Routinen zum Speichern neuer Agenten (DB oder YAML)
- [x] Eingaben: Name, Beschreibung, Spezialisierung, Fähigkeiten
- [x] Validierung und Tests der Eingaben

## Milestone 18: Tool-Baukasten & Registrierung
- [x] Editor zum Definieren neuer Tools (Name, Beschreibung, Kommando, Parameter)
- [x] Tools persistent speichern und beim App-Start laden
- [x] Zuordnung von Tools zu Agenten in der UI ermöglichen
- [x] Registrierung der Tools im System prüfen
- [x] Tests für Tool-Verwaltung und -Zuordnung

## Milestone 19: Integration in Queen- und Agentensystem
- [x] Queen lädt neue Agenten automatisch und aktiviert sie
- [x] Deaktivierung einzelner Agenten über die GUI
- [x] Controller erlaubt dynamische Auswahl aller registrierten Agenten
- [x] Dokumentation aktualisieren und Beispiele ergänzen


## Milestone 20: Zentrale Kontext-Engine
- [x] Kontextdatenstruktur `context_state.json` anlegen und laden
- [x] Felder: `history`, `agents`, `task_flow`, `handoffs`, `user_actions`
- [x] Live-Aktualisierung und optionale Speicherung in der DB
- [x] Kontext-API zum Lesen und Schreiben aller Bereiche
- [x] UI-Komponente zur Anzeige des aktuellen Gesamtzustands
- [x] Tests und Dokumentation der Funktion
