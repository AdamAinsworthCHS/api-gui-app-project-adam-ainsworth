"""
trivia.py
by Adam Ainsworth
Main interface for the trivia game
"""

"""
start.py
by Adam Ainsworth
Start page for the trivia game
"""

import sys
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QStackedLayout,
    QStackedWidget
)

class TriviaWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        # create layout
        self.layout = QVBoxLayout()

        # add labels
        self.title = QLabel("game")

        # add button
        self.begin_game_button = QPushButton("Back to main menu")
        # self.begin_game_button.clicked.connect(self.MainMenu)

        # add widgets & layouts to main layout
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.begin_game_button)

        widget = QWidget()
        widget.setLayout(self.layout)

    # def MainMenu(self):
    #     window = start.MainWindow()
    #     window.show()