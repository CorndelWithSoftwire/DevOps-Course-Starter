import requests
import os

def get_cards_for_board():
    board_id = os.getenv("TRELLO_BOARD_ID")
    key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_API_TOKEN")

    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    params = { "key": key, "token": token }
    response = requests.get(url, params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Wrong status on cards response: {response.status_code}")