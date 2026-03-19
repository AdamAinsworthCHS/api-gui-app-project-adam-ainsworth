"""
controller.py
by Adam Ainsworth
Controller for the trivia game
"""

import requests

url = "https://www.fruityvice.com/api/fruit/all"
response = requests.get(url)
data = response.json()
fruitDict = {}
fruitDict = data