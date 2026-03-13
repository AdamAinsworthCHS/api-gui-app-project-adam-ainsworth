"""
api_testing.py
by Adam Ainsworth
Api stuff
"""

import sys
import requests
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QWidget
)

# q applicaiton
app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fruit Api")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 400)

        # create layout
        layout = QVBoxLayout()

        # add labels
        instructions = QLabel("Push a button, get FRUIT DATA")
        self.output = QLabel("Output: ")

        # add button
        self.apple_button = QPushButton("Persimmon")
        self.apple_button.clicked.connect(self.GiveDataPersimmon)
        self.blackberry_button = QPushButton("Strawberry")
        self.blackberry_button.clicked.connect(self.GiveDataStrawberry)
        self.mango_button = QPushButton("Banana")
        self.mango_button.clicked.connect(self.GiveDataBanana)

        # add widgets & layouts to main layout
        layout.addWidget(instructions)
        layout.addWidget(self.apple_button)
        layout.addWidget(self.blackberry_button)
        layout.addWidget(self.mango_button)
        layout.addWidget(self.output)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def GiveDataPersimmon(self):
        self.output.setText("Output: " + str(fruitDict[0]['name']) + ", Calories/100g: " + str(fruitDict[0]['nutritions']['calories']))
    
    def GiveDataStrawberry(self):
        self.output.setText("Output: " + str(fruitDict[1]['name']) + ", Calories/100g: " + str(fruitDict[1]['nutritions']['calories']))

    def GiveDataBanana(self):
        self.output.setText("Output: " + str(fruitDict[2]['name']) + ", Calories/100g: " + str(fruitDict[2]['nutritions']['calories']))

        


if __name__ == "__main__":
    window = MainWindow()
    window.show()

    url = "https://www.fruityvice.com/api/fruit/all"
    response = requests.get(url)
    data = response.json()
    fruitDict = {}
    fruitDict = data

    app.exec()