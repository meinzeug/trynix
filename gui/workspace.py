from __future__ import annotations

from PySide6 import QtWidgets, QtCore
from pathlib import Path
import shutil

from .python_highlighter import PythonHighlighter


class WorkspaceViewer(QtWidgets.QMainWindow):
    """Display workspace folder with live file view."""

    def __init__(self, workspace: Path) -> None:
        super().__init__()
        self.workspace = workspace
        self.setWindowTitle(f"Workspace - {workspace.name}")

        self.model = QtWidgets.QFileSystemModel(self)
        self.model.setRootPath(str(workspace))
        self.tree = QtWidgets.QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(str(workspace)))
        self.tree.setHeaderHidden(True)

        self.editor = QtWidgets.QPlainTextEdit(readOnly=True)
        self.highlighter = PythonHighlighter(self.editor.document())

        self.export_btn = QtWidgets.QPushButton("Export ZIP")

        splitter = QtWidgets.QSplitter()
        splitter.addWidget(self.tree)
        splitter.addWidget(self.editor)

        central = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(central)
        layout.addWidget(splitter)
        layout.addWidget(self.export_btn)
        self.setCentralWidget(central)

        self.tree.selectionModel().currentChanged.connect(self.display_file)
        self.export_btn.clicked.connect(self.export_zip)

    def display_file(self, current: QtCore.QModelIndex) -> None:
        path = Path(self.model.filePath(current))
        if path.is_file():
            try:
                text = path.read_text(encoding="utf-8")
            except Exception:
                text = ""
            self.editor.setPlainText(text)

    def export_zip(self) -> None:
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export Workspace", str(self.workspace.name) + ".zip", "Zip Files (*.zip)"
        )
        if path:
            try:
                shutil.make_archive(Path(path).with_suffix(""), "zip", self.workspace)
                QtWidgets.QMessageBox.information(self, "Export", "ZIP exported")
            except Exception as exc:
                QtWidgets.QMessageBox.warning(self, "Export", str(exc))
