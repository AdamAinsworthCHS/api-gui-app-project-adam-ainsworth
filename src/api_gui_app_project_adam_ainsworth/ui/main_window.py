"""
start.py
by Adam Ainsworth
Start page for the trivia game
"""

import sys
from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QLabel,
    QWidget,
    QStackedLayout,
    QGridLayout
)
import utils.controller
from ui.trivia import TriviaWindow
from ui.results import ResultsWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FruiTrivia")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        # Create a stacked layout for multiple screens
        self.stacked_layout = QStackedLayout()

        # Main page: 
        self.main_page = QWidget()
        self.main_layout = QGridLayout()
        title_label = QLabel("FruiTrivia")
        self.trivia_button = QPushButton("Begin Game")
        self.trivia_button.clicked.connect(lambda: self.goto_page(1))
        self.main_layout.addWidget(title_label, 0, 0, 1, 3)
        self.main_layout.addWidget(self.trivia_button, 1, 0, 1, 1)
        self.main_page.setLayout(self.main_layout)

        # Trivia page: 
        self.trivia_page = TriviaWindow(self)
        self.results_page = ResultsWindow(self)

        # add widgets & layouts to main layout
        self.stacked_layout.addWidget(self.main_page)
        self.stacked_layout.addWidget(self.trivia_page)
        self.stacked_layout.addWidget(self.results_page)

        widget = QWidget()
        widget.setLayout(self.stacked_layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def goto_page(self, destination):
        self.stacked_layout.setCurrentIndex(destination)