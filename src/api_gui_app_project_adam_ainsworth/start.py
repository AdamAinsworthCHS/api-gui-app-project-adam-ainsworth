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
    QStackedWidget,
    QStackedLayout,
    QGridLayout
)
import controller

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
        self.trivia_button.clicked.connect(self.goto_page)
        self.main_layout.addWidget(title_label, 0, 0, 1, 3)
        self.main_layout.addWidget(self.trivia_button, 1, 0, 1, 1)
        self.main_page.setLayout(self.main_layout)

        # Trivia page: 
        self.trivia_page = QWidget()
        self.trivia_layout = QGridLayout()
        trivia_label = QLabel("Trivia Game")
        self.main_menu_button = QPushButton("Main Menu")
        self.main_menu_button.clicked.connect(self.goto_page)
        self.trivia_layout.addWidget(trivia_label, 0, 0, 1, 3)
        self.trivia_layout.addWidget(self.main_menu_button, 1, 0, 1, 1)
        self.trivia_page.setLayout(self.trivia_layout)

        # add widgets & layouts to main layout
        self.stacked_layout.addWidget(self.main_page)
        self.stacked_layout.addWidget(self.trivia_page)

        widget = QWidget()
        widget.setLayout(self.stacked_layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def goto_page(self):
        sending_button = self.sender()
        if sending_button.text() == "Begin Game":
            self.stacked_layout.setCurrentIndex(1)
        elif sending_button.text() == "Main Menu":
            self.stacked_layout.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()