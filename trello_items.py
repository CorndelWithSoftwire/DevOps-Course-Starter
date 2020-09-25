import os
import requests

board_id = os.getenv('TRELLO_BOARD_ID')
api_key = os.getenv('TRELLO_API_KEY')
api_secret = os.getenv('TRELLO_API_SECRET')

def get_cards():
    response = requests.get(f'http://api.trello.com/1/boards/{board_id}/cards', params ={'key': api_key, 'token': api_secret})
    return response.json()

def get_cards_list(card_id):
    response = requests.get(f'https://api.trello.com/1/cards/{card_id}/list', params ={'key': api_key, 'token': api_secret})
    return response.json()

#def update_cards_to_complete(card_id)
 #   requests.put('')