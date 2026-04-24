"""
start.py
by Adam Ainsworth
Start page for the trivia game
"""

import sys
from PySide6.QtWidgets import QApplication
import ui.main_window
from PySide6.QtGui import QFont, QFontDatabase

if __name__ == "__main__":
    app = QApplication(sys.argv)
    font_id = QFontDatabase.addApplicationFont("resources/fonts/Bestime.ttf")
    bestime_font = QFontDatabase.applicationFontFamilies(font_id)[0]
    font_id = QFontDatabase.addApplicationFont("resources/fonts/pixelsplitter.ttf")
    pixelsplitter_font = QFontDatabase.applicationFontFamilies(font_id)[0]
    app.setStyleSheet(
    """
    QLabel {
        background-color: #acf09e;
        color: #000000;
        font-family: bestime;
        font-size: 25px;
    }
    QPushButton {
        background-color: #d1ffd6;
        color: #000000;
        font-family: pixelsplitter;
        font-size: 13px;
    }
    QMainWindow {
        background-color: #acf09e;
        color: #000000;
        font-family: bestime;
        font-size: 13px;
    }
    """
    )
    window = ui.main_window.MainWindow()
    window.show()

    app.exec()