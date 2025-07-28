from __future__ import annotations

from PySide6 import QtWidgets

from .python_highlighter import PythonHighlighter

from db import get_code_files


class CodeViewer(QtWidgets.QMainWindow):
    def __init__(self, conn, project_id: int) -> None:
        super().__init__()
        self.conn = conn
        self.project_id = project_id
        self.setWindowTitle("Code Viewer")

        self.file_list = QtWidgets.QListWidget()
        self.save_btn = QtWidgets.QPushButton("Save File")
        self.editor = QtWidgets.QPlainTextEdit(readOnly=True)
        self.highlighter = PythonHighlighter(self.editor.document())

        central = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(central)

        left_layout = QtWidgets.QVBoxLayout()
        left_layout.addWidget(self.file_list)
        left_layout.addWidget(self.save_btn)

        layout.addLayout(left_layout)
        layout.addWidget(self.editor)
        self.setCentralWidget(central)

        self.file_list.itemSelectionChanged.connect(self.display_file)
        self.save_btn.clicked.connect(self.save_file)
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

    def save_file(self) -> None:
        row = self.file_list.currentRow()
        if row < 0:
            return
        data = self.files[row]
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", data["path"])
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(data["content"] or "")
                QtWidgets.QMessageBox.information(self, "Save File", "File saved")
            except Exception as exc:
                QtWidgets.QMessageBox.warning(self, "Save File", str(exc))
