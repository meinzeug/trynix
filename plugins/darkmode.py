"""Simple plugin to apply a dark theme."""

from __future__ import annotations

from PySide6 import QtGui, QtWidgets


class Plugin:
    def register(self, app: QtWidgets.QApplication) -> None:
        app.setStyle("Fusion")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(35, 35, 35))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Text, QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.BrightText, QtGui.QColor(255, 0, 0))
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197))
        palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(0, 0, 0))
        app.setPalette(palette)

