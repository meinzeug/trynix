from __future__ import annotations

from PySide6 import QtWidgets
from pathlib import Path
import json

from db import get_project


class RoadmapWindow(QtWidgets.QWidget):
    def __init__(self, conn, project_id: int) -> None:
        super().__init__()
        self.conn = conn
        self.project_id = project_id
        self.setWindowTitle("Roadmap")

        self.tree = QtWidgets.QTreeWidget()
        self.tree.setHeaderLabels(["Item", "Status"])

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.tree)

        self.load_roadmap()

    def load_roadmap(self) -> None:
        row = get_project(self.conn, self.project_id)
        if not row or not row["roadmap"]:
            return
        path = Path(row["roadmap"])
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return
        self.tree.clear()
        for ms in data.get("milestones", []):
            item = QtWidgets.QTreeWidgetItem([ms.get("title", ""), ms.get("status", "")])
            self.tree.addTopLevelItem(item)
            for task in ms.get("tasks", []):
                QtWidgets.QTreeWidgetItem(item, [task.get("title", ""), task.get("status", "")])
        self.tree.expandAll()
