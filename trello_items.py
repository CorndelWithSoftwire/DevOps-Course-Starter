import os
import requests

def get_cards():
    board_id = os.getenv('TRELLO_BOARD_ID')
    api_key = os.getenv('TRELLO_API_KEY')
    api_secret = os.getenv('TRELLO_API_SECRET')
    response = requests.get(f'http://api.trello.com/1/boards/{board_id}/cards', params ={'key': api_key, 'token': api_secret})
    return response.json()

def update_carde_to_complete(card_id)
    requests.put('')