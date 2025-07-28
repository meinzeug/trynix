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
- [ ] Queen-Nachrichten automatisch ueber TTS ausgeben
- [ ] Schalter in den Einstellungen zum Aktivieren/Deaktivieren

## Milestone 11: Agenten-Plugin-System
- [x] Plugin-Schnittstelle erweitern, um neue Agenten einzubinden
- [ ] Beispielplugin fuer einen Custom-Agent bereitstellen

## Milestone 12: Live-Projekt-Workspace & ZIP-Export
- [ ] Zentrales Verzeichnis `workspace/` anlegen
- [ ] Unterordner `<projektname-timestamp>` bei jedem Agentenlauf erstellen
- [ ] Dateibaum in der GUI mit `QFileSystemModel` live anzeigen
- [ ] Dateien per Klick in schreibgeschütztem Editor mit Syntaxhighlighting öffnen
- [ ] Änderungen am Workspace in Echtzeit verfolgen
- [ ] Projektordner über einen Button als ZIP exportieren
- [ ] Archivierung mit `shutil.make_archive` implementieren
- [ ] Pfadverwaltung und DB-Eintrag für den Workspace ergänzen

## Milestone 13: Dynamische Roadmap & Queen-Dialog
- [ ] Queen erzeugt aus der Nutzeridee automatisch ein vollständiges Konzept
  (Funktionsübersicht, Struktur und Technologieeinsatz).
- [ ] Generierte Roadmap mit Meilensteinen und Subtasks dauerhaft speichern
  (JSON-Datei und DB-Eintrag).
- [ ] GUI zeigt eine Live-Roadmap-Ansicht mit Status (offen/in Arbeit/erledigt).
- [ ] Queen überwacht die Roadmap und markiert erledigte Punkte automatisch.
- [ ] Änderungswünsche lassen sich über Chat oder Spracheingabe einreichen.
- [ ] Nach Bestätigung durch die Queen wird die Roadmap angepasst und erneut
  gespeichert.

## Milestone 14: Zauberstab - automatische Feature-Innovation
- [ ] Zauberstab-Icon (🪄) in der GUI mit Tooltip "Lass die Queen neue Features vorschlagen"
- [ ] Klick analysiert Codebasis unter `workspace/` sowie `milestones.md`
- [ ] Queen entwickelt daraus 2–5 neue Feature-Ideen inkl. Nutzenbeschreibung
- [ ] Ideen erscheinen in einem Panel mit Button "Zur Roadmap hinzufügen"
- [ ] Akzeptierte Vorschläge werden als neuer Milestone mit Subtasks in `milestones.md` eingetragen
- [ ] Optional Notizen zu den Features in `brain.md` speichern
- [ ] Ergebnis und Aktionen im Chat/Log dokumentieren
- [ ] Tests und Dokumentation der Funktion anlegen

