from flask import session
import requests
from trello_cards import make_trello_auth, get_cards_url_with_auth
import os

def get_items():
    """ Simple attempt to get all cards from Trello. """
    response = requests.get(make_trello_auth(f"https://api.trello.com/1/boards/{os.environ['BOARD_ID']}/cards"))
    todos = response.json()
    for card in todos:
        print(card ['name'], card['desc'])        
    return todos


def get_done_items():
    """ Simple attempt to get all done cards from Trello. """
    response = requests.get(f"https://api.trello.com/1/lists/{os.getenv('DONE_idList')}/cards?key={os.getenv('TRELLO_API_KEY')}&token={os.getenv('TRELLO_API_TOKEN')}")

    todos = response.json()
    for card in todos:
        print(card['name'], card['desc'])
    return todos
    

def add_new_item(name, desc):
    create_new_card = {'idList': os.getenv('TODO_idList'), 'name': name, 'desc': desc}
    response = requests.post(get_cards_url_with_auth(), params=create_new_card)
    return response


def update_item(id):

    params={"key": os.getenv('TRELLO_API_KEY'), "token": os.getenv('TRELLO_API_TOKEN'), "idList": os.getenv('DONE_idList')}

    response=requests.put(f"https://api.trello.com/1/cards/{os.getenv('DOING_CARD_ID')}", params=params)                 

    return response


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)

def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item

def delete_item(item):

    existing_items = get_items()
    existing_items.remove(item)
    updated_items = existing_items
    session['items'] = updated_items
    return item
