"""
results.py
by Adam Ainsworth
Results screen for the trivia game
"""

import sys
from PySide6.QtWidgets import (
    QPushButton,
    QLabel,
    QWidget,
    QVBoxLayout
)
import random
import utils.controller
from PySide6.QtCore import Qt

class ResultsWindow(QWidget):

    def __init__(self, parent_self):
        super().__init__()

        self.correct = 0

        self.results_page = QWidget()
        self.results_layout = QVBoxLayout()
        self.results_label = QLabel("")
        self.setLayout(self.results_layout)
        self.trivia_button = QPushButton("Next Question")
        self.trivia_button.clicked.connect(lambda: self.NextQuestion(parent_self))
        
        self.results_layout.addWidget(self.results_label, 0, alignment=Qt.AlignCenter)
        self.results_layout.addWidget(self.trivia_button, 1, alignment=Qt.AlignCenter)
    
    def update_correct(self):
        self.correct += 1
        self.results_label.setText("Correct! \nTotal Correct: " + str(self.correct))
    
    def update_wrong(self):
        self.results_label.setText("Incorrect. \nTotal Correct: " + str(self.correct))
    
    def NextQuestion(self, parent_self):
        parent_self.trivia_page.CreateQuestion(parent_self)
        parent_self.stacked_layout.setCurrentIndex(1)