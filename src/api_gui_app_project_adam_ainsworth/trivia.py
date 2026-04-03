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
import results

class TriviaWindow(QWidget):

    def __init__(self, parent_self):
        super().__init__()

        self.trivia_page = QWidget()
        self.trivia_layout = QGridLayout()
        self.trivia_label = QLabel("Trivia Game")
        self.setLayout(self.trivia_layout)

        # question vars
        self.fruit = 0
        self.category = 0
        self.fruits = []
        self.correct_button = 0

        self.first_fruit_button = QPushButton("-")
        self.second_fruit_button = QPushButton("-")
        self.third_fruit_button = QPushButton("-")
        self.fourth_fruit_button = QPushButton("-")

        self.CreateQuestion(parent_self)
        
        self.trivia_layout.addWidget(self.trivia_label, 0, 0, 1, 3)
        self.trivia_layout.addWidget(self.first_fruit_button, 1, 0, 1, 1)
        self.trivia_layout.addWidget(self.second_fruit_button, 2, 0, 1, 1)
        self.trivia_layout.addWidget(self.third_fruit_button, 3, 0, 1, 1)
        self.trivia_layout.addWidget(self.fourth_fruit_button, 4, 0, 1, 1)

        
    
    def CreateQuestion(self, parent_self):
        self.first_fruit_button.clicked.disconnect()
        self.second_fruit_button.clicked.disconnect()
        self.third_fruit_button.clicked.disconnect()
        self.fourth_fruit_button.clicked.disconnect()
        self.fruits.clear()
        self.correct_button = random.randrange(5)
        self.category = random.randrange(6)
        while self.fruits.__len__() < 6:
            tempnumber = 0
            tempnumber = random.randrange(49)
            if self.fruits.__contains__(tempnumber):
                pass
            else:
                self.fruits.append(tempnumber)
        
        if (self.category == 1):
            temp_calories_number = 0
            for i in range (self.fruits.__len__()):
                if controller.fruitDict[self.fruits[i]]['nutritions']['calories'] > temp_calories_number:
                    temp_calories_number = controller.fruitDict[self.fruits[i]]['nutritions']['calories']
                    self.fruit = self.fruits[i]
            self.fruits.remove(self.fruit)
            self.trivia_label.setText("Which fruit has the most calories per 100 grams?")
        elif (self.category == 2):
            temp_fat_number = 0
            for i in range (self.fruits.__len__()):
                if controller.fruitDict[self.fruits[i]]['nutritions']['fat'] > temp_fat_number:
                    temp_fat_number = controller.fruitDict[self.fruits[i]]['nutritions']['fat']
                    self.fruit = self.fruits[i]
            self.fruits.remove(self.fruit)
            self.trivia_label.setText("Which fruit has the most fat per 100 grams?")
        elif (self.category == 3):
            temp_sugar_number = 0
            for i in range (self.fruits.__len__()):
                if controller.fruitDict[self.fruits[i]]['nutritions']['sugar'] > temp_sugar_number:
                    temp_sugar_number = controller.fruitDict[self.fruits[i]]['nutritions']['sugar']
                    self.fruit = self.fruits[i]
            self.fruits.remove(self.fruit)
            self.trivia_label.setText("Which fruit has the most sugar per 100 grams?")
        elif (self.category == 4):
            temp_carbs_number = 0
            for i in range (self.fruits.__len__()):
                if controller.fruitDict[self.fruits[i]]['nutritions']['carbohydrates'] > temp_carbs_number:
                    temp_carbs_number = controller.fruitDict[self.fruits[i]]['nutritions']['carbohydrates']
                    self.fruit = self.fruits[i]
            self.fruits.remove(self.fruit)
            self.trivia_label.setText("Which fruit has the most carbohydrates per 100 grams?")
        elif (self.category == 5):
            temp_protein_number = 0
            for i in range (self.fruits.__len__()):
                if controller.fruitDict[self.fruits[i]]['nutritions']['protein'] > temp_protein_number:
                    temp_protein_number = controller.fruitDict[self.fruits[i]]['nutritions']['protein']
                    self.fruit = self.fruits[i]
            self.fruits.remove(self.fruit)
            self.trivia_label.setText("Which fruit has the most protein per 100 grams?")
        
        if self.correct_button == 1:
            self.first_fruit_button.setText(controller.fruitDict[self.fruit]['name'])
            self.first_fruit_button.clicked.connect(lambda: self.CorrectAnswer(parent_self))
        else:
            self.first_fruit_button.setText(controller.fruitDict[self.fruits[0]]['name'])
            self.first_fruit_button.clicked.connect(lambda: self.WrongAnswer(parent_self))
        
        if self.correct_button == 2:
            self.second_fruit_button.setText(controller.fruitDict[self.fruit]['name'])
            self.second_fruit_button.clicked.connect(lambda: self.CorrectAnswer(parent_self))
        else:
            self.second_fruit_button.setText(controller.fruitDict[self.fruits[1]]['name'])
            self.second_fruit_button.clicked.connect(lambda: self.WrongAnswer(parent_self))
        
        if self.correct_button == 3:
            self.third_fruit_button.setText(controller.fruitDict[self.fruit]['name'])
            self.third_fruit_button.clicked.connect(lambda: self.CorrectAnswer(parent_self))
        else:
            self.third_fruit_button.setText(controller.fruitDict[self.fruits[2]]['name'])
            self.third_fruit_button.clicked.connect(lambda: self.WrongAnswer(parent_self))

        if self.correct_button == 4:
            self.fourth_fruit_button.setText(controller.fruitDict[self.fruit]['name'])
            self.fourth_fruit_button.clicked.connect(lambda: self.CorrectAnswer(parent_self))
        else:
            self.fourth_fruit_button.setText(controller.fruitDict[self.fruits[3]]['name'])
            self.fourth_fruit_button.clicked.connect(lambda: self.WrongAnswer(parent_self))
    
    def WrongAnswer(self, parent_self):
        results.ResultsWindow.update_wrong(parent_self.results_page)
        parent_self.stacked_layout.setCurrentIndex(2)

    def CorrectAnswer(self, parent_self):
        results.ResultsWindow.update_correct(parent_self.results_page)
        parent_self.stacked_layout.setCurrentIndex(2)