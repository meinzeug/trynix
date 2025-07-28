from __future__ import annotations

from PySide6 import QtWidgets

from db import get_code_files


class CodeViewer(QtWidgets.QMainWindow):
    def __init__(self, conn, project_id: int) -> None:
        super().__init__()
        self.conn = conn
        self.project_id = project_id
        self.setWindowTitle("Code Viewer")

        self.file_list = QtWidgets.QListWidget()
        self.editor = QtWidgets.QPlainTextEdit(readOnly=True)

        central = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(central)
        layout.addWidget(self.file_list)
        layout.addWidget(self.editor)
        self.setCentralWidget(central)

        self.file_list.itemSelectionChanged.connect(self.display_file)
        self.load_files()

    def load_files(self) -> None:
        self.files = get_code_files(self.conn, self.project_id)
        self.file_list.clear()
        for row in self.files:
            self.file_list.addItem(row["path"])

    def display_file(self) -> None:
        row = self.file_list.currentRow()
        if row >= 0:
            data = self.files[row]
            self.editor.setPlainText(data["content"] or "")
