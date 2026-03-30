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
import random
import controller

class TriviaWindow(QWidget):

    def __init__(self, parentSelf):
        super().__init__()

        self.trivia_page = QWidget()
        self.trivia_layout = QGridLayout()
        trivia_label = QLabel("Trivia Game")
        self.setLayout(self.trivia_layout)

        # question vars
        self.fruit = 0
        self.category = 0
        self.otherfruits = []
        correct_button = random.randrange(5)

        self.CreateQuestion()
        if (self.category == 1):
            trivia_label.setText("Which fruit has " + str(controller.fruitDict[self.fruit]['nutritions']['calories']) + " calories per 100 grams?")
        elif (self.category == 2):
            trivia_label.setText("Which fruit has " + str(controller.fruitDict[self.fruit]['nutritions']['fat']) + " grams of fat per 100 grams of fruit?")
        elif (self.category == 3):
            trivia_label.setText("Which fruit has " + str(controller.fruitDict[self.fruit]['nutritions']['sugar']) + " grams of sugar per 100 grams of fruit?")
        elif (self.category == 4):
            trivia_label.setText("Which fruit has " + str(controller.fruitDict[self.fruit]['nutritions']['carbohydrates']) + " grams of carbohydrates per 100 grams of fruit?")
        elif (self.category == 5):
            trivia_label.setText("Which fruit has " + str(controller.fruitDict[self.fruit]['nutritions']['protein']) + " grams of protein per 100 grams of fruit?")
        
        if correct_button == 1:
            self.first_fruit_button = QPushButton(controller.fruitDict[self.fruit]['name'])
            self.first_fruit_button.clicked.connect(self.CorrectAnswer)
        else:
            self.first_fruit_button = QPushButton(controller.fruitDict[self.otherfruits[0]]['name'])
            self.first_fruit_button.clicked.connect(self.WrongAnswer)
        
        if correct_button == 2:
            self.second_fruit_button = QPushButton(controller.fruitDict[self.fruit]['name'])
            self.second_fruit_button.clicked.connect(self.CorrectAnswer)
        else:
            self.second_fruit_button = QPushButton(controller.fruitDict[self.otherfruits[1]]['name'])
            self.second_fruit_button.clicked.connect(self.WrongAnswer)
        
        if correct_button == 3:
            self.third_fruit_button = QPushButton(controller.fruitDict[self.fruit]['name'])
            self.third_fruit_button.clicked.connect(self.CorrectAnswer)
        else:
            self.third_fruit_button = QPushButton(controller.fruitDict[self.otherfruits[2]]['name'])
            self.third_fruit_button.clicked.connect(self.WrongAnswer)
        
        if correct_button == 4:
            self.fourth_fruit_button = QPushButton(controller.fruitDict[self.fruit]['name'])
            self.fourth_fruit_button.clicked.connect(self.CorrectAnswer)
        else:
            self.fourth_fruit_button = QPushButton(controller.fruitDict[self.otherfruits[3]]['name'])
            self.fourth_fruit_button.clicked.connect(self.WrongAnswer)
        
        self.trivia_layout.addWidget(trivia_label, 0, 0, 1, 3)
        self.trivia_layout.addWidget(self.first_fruit_button, 1, 0, 1, 1)
        self.trivia_layout.addWidget(self.second_fruit_button, 2, 0, 1, 1)
        self.trivia_layout.addWidget(self.third_fruit_button, 3, 0, 1, 1)
        self.trivia_layout.addWidget(self.fourth_fruit_button, 4, 0, 1, 1)
    
    def CreateQuestion(self):
        self.fruit = random.randrange(49)
        self.category = random.randrange(6)
        while self.otherfruits.__len__() < 4:
            tempnumber = 0
            tempnumber = random.randrange(49)
            if tempnumber != self.fruit:
                if self.otherfruits.__contains__(tempnumber):
                    pass
                else:
                    self.otherfruits.append(tempnumber)
    
    def WrongAnswer(self):
        print("wrong")

    def CorrectAnswer(self):
        print("right")