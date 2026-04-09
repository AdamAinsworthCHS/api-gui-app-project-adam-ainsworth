"""
controller.py
by Adam Ainsworth
utils.controller for the trivia game
"""

import requests as re
import json

url = "https://www.fruityvice.com/api/fruit/all"
response = re.get(url)
data = response.json()
fruitDict = {}
fruitDict = data
    
