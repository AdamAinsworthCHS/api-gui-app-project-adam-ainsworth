"""
controller.py
by Adam Ainsworth
utils.controller for the trivia game
"""

import requests as re
import json

fruit_dict = {}

def PullData(base_url: str, endpoint="", query="") -> dict:
    url = base_url + endpoint + query
    # make the call
    try:
        response = re.get(url, timeout=5)

        # raises an error for 4xx and 5xx status codes
        response.raise_for_status()
        if response.ok:
            return response.json()
        else:
            return f"Something went wrong"
    
    except re.exceptions.RequestException as e:
        return f"Something went wrong: {e}"

def SaveData(data):
    with open('data/fruit_dict.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def LoadData():
    with open('data/fruit_dict.json', 'r') as file:
        data = json.load(file)
        return data

if __name__ == "__main__":
    # Make api requests
    base_api = "https://www.fruityvice.com/api/"
    endpoint = "fruit/"
    search_term = "all"
    fruit_data = PullData(base_api, endpoint, search_term)
    if isinstance(fruit_data, str):
        print(fruit_data)
    else:
        SaveData(fruit_data)
    fruit_dict = LoadData()
else:
    # Make api requests
    base_api = "https://www.fruityvice.com/api/"
    endpoint = "fruit/"
    search_term = "all"
    fruit_data = PullData(base_api, endpoint, search_term)
    if isinstance(fruit_data, str):
        print(fruit_data)
    else:
        SaveData(fruit_data)
    fruit_dict = LoadData()