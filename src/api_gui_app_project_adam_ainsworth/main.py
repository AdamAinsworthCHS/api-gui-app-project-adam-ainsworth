"""
start.py
by Adam Ainsworth
Start page for the trivia game
"""

import sys
from PySide6.QtWidgets import QApplication
import ui.main_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ui.main_window.MainWindow()
    window.show()

    app.exec()