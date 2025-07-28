from __future__ import annotations

from PySide6 import QtGui, QtCore


class PythonHighlighter(QtGui.QSyntaxHighlighter):
    """Very small syntax highlighter for Python code."""

    KEYWORDS = [
        'False', 'class', 'finally', 'is', 'return',
        'None', 'continue', 'for', 'lambda', 'try',
        'True', 'def', 'from', 'nonlocal', 'while',
        'and', 'del', 'global', 'not', 'with',
        'as', 'elif', 'if', 'or', 'yield',
        'assert', 'else', 'import', 'pass',
        'break', 'except', 'in', 'raise',
    ]

    def __init__(self, document: QtGui.QTextDocument) -> None:
        super().__init__(document)
        self.rules: list[tuple[QtCore.QRegularExpression, QtGui.QTextCharFormat]] = []

        keyword_format = QtGui.QTextCharFormat()
        keyword_format.setForeground(QtGui.QColor("blue"))
        for word in self.KEYWORDS:
            pattern = QtCore.QRegularExpression(rf"\b{word}\b")
            self.rules.append((pattern, keyword_format))

        string_format = QtGui.QTextCharFormat()
        string_format.setForeground(QtGui.QColor("magenta"))
        self.rules.append((QtCore.QRegularExpression(r"'[^'\\n]*'"), string_format))
        self.rules.append((QtCore.QRegularExpression(r'"[^"\\n]*"'), string_format))

        comment_format = QtGui.QTextCharFormat()
        comment_format.setForeground(QtGui.QColor("darkgreen"))
        self.rules.append((QtCore.QRegularExpression(r"#.*"), comment_format))

    def highlightBlock(self, text: str) -> None:  # pragma: no cover - GUI
        for pattern, fmt in self.rules:
            it = pattern.globalMatch(text)
            while it.hasNext():
                match = it.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), fmt)

