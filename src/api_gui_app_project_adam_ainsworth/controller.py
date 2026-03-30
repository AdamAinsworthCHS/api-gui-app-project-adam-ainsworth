"""
controller.py
by Adam Ainsworth
Controller for the trivia game
"""

import requests
import random

url = "https://www.fruityvice.com/api/fruit/all"
response = requests.get(url)
data = response.json()
fruitDict = {}
fruitDict = data

def CreateQuestion():
    fruit = random.randrange(49)
    category = random.randrange(6)
    
