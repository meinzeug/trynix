from __future__ import annotations

from PySide6 import QtWidgets
from pathlib import Path

from db import add_message, get_project
from services import suggest_features, add_milestone


class WandWindow(QtWidgets.QWidget):
    """Show feature suggestions from the Queen."""

    def __init__(self, conn, project_id: int) -> None:
        super().__init__()
        self.conn = conn
        self.project_id = project_id
        self.setWindowTitle("Feature Wizard")

        self.list = QtWidgets.QListWidget()
        self.add_btn = QtWidgets.QPushButton("Zur Roadmap hinzufügen")

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.list)
        layout.addWidget(self.add_btn)

        self.add_btn.clicked.connect(self.add_selected)
        self.ideas = []
        self.load_ideas()

    def load_ideas(self) -> None:
        row = get_project(self.conn, self.project_id)
        workspace = Path(row["workspace"] or "workspace") if row else Path("workspace")
        ideas = suggest_features(workspace, Path("codex/daten/milestones.md"))
        self.ideas = ideas
        for idea in ideas:
            self.list.addItem(f"{idea['title']}: {idea['description']}")

    def add_selected(self) -> None:
        row = self.list.currentRow()
        if row < 0:
            return
        idea = self.ideas[row]
        add_milestone(idea, Path("codex/daten/milestones.md"))
        with Path("codex/daten/brain.md").open("a", encoding="utf-8") as f:
            f.write(f"- Neue Feature-Idee aufgenommen: {idea['title']}\n")
        add_message(self.conn, self.project_id, "queen", f"Feature added: {idea['title']}")
        QtWidgets.QMessageBox.information(self, "Roadmap", "Feature hinzugefügt")

