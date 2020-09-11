from flask import session
import requests
from trello_cards import make_trello_auth, get_cards_url_with_auth
import os

def get_items():
    """ Simple attempt to get all cards from Trello. """
    response = requests.get(make_trello_auth(f"https://api.trello.com/1/boards/{os.getenv('BOARD_ID')}/cards"))
    todos = response.json()
    for card in todos:
        print(card ['name'], card['desc'])        
    return todos


def get_done_items():
    """ Simple attempt to get all done cards from Trello. """
    response = requests.get(f"https://api.trello.com/1/lists/{os.getenv('DONE_idList')}/cards?key={os.getenv('TRELLO_API_KEY')}&token={os.getenv('TRELLO_API_TOKEN')}")

    dones = response.json()
    for card in dones:
        print(card['name'], card['desc'])
    return dones
    

def add_new_item(name, desc):
    create_new_card = {'idList': os.getenv('TODO_idList'), 'name': name, 'desc': desc}
    response = requests.post(get_cards_url_with_auth(), params=create_new_card)
    return response


def update_item(id):
    params={"key": os.getenv('TRELLO_API_KEY'), "token": os.getenv('TRELLO_API_TOKEN'), "idList": os.getenv('DONE_idList')}
    response=requests.put(f"https://api.trello.com/1/cards/{os.getenv('DOING_CARD_ID')}", params=params)                 
    return response

def get_id_of_card():
    params = {"key": os.getenv('TRELLO_API_KEY'), "token": os.getenv('TRELLO_API_TOKEN')}
    response = requests.get(
        f"https://api.trello.com/1/cards/{os.getenv('DOING_CARD_ID')}/labels?", params=params)

    return response[id]

def delete_item():

    params = {"key": os.getenv('TRELLO_API_KEY'), "token": os.getenv('TRELLO_API_TOKEN')}
    response = requests.delete(f"https://api.trello.com/1/cards/{os.getenv('DOING_CARD_ID')}", params=params)
    return response


