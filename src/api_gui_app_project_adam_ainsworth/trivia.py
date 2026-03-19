"""
trivia.py
by Adam Ainsworth
Main interface for the trivia game
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
    QStackedWidget,
    QGridLayout
)

class TriviaWindow(QWidget):
    def __init__(self, parentSelf):
        super().__init__()

        self.trivia_page = QWidget()
        self.trivia_layout = QGridLayout()
        trivia_label = QLabel("Trivia Game")
        self.main_menu_button = QPushButton("Main Menu")
        self.main_menu_button.clicked.connect(parentSelf.goto_page)
        self.trivia_layout.addWidget(trivia_label, 0, 0, 1, 3)
        self.trivia_layout.addWidget(self.main_menu_button, 1, 0, 1, 1)
        self.setLayout(self.trivia_layout)