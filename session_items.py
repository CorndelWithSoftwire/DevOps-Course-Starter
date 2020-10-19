from flask import session

import requests
import os

from requests.models import HTTPError
from todo_item import TodoItem
from flask import current_app as app

_DEFAULT_ITEMS = []

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    # return session.get('items', _DEFAULT_ITEMS)
    payload = {'key': os.getenv('TRELLO_KEY'), 'token': os.getenv('TRELLO_TOKEN')}
    r = requests.get(f'https://api.trello.com/1/boards/{os.getenv("TRELLO_BOARD_ID")}/cards', params=payload)
    list = []
 
    for item in r.json():
        list_item = TodoItem(item["id"], item['name'], item["idList"])
        list.append(list_item)
 
    return list


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    payload = {
        'key': os.getenv('TRELLO_KEY'), 
        'token': os.getenv('TRELLO_TOKEN'),
        'idList': os.getenv('TRELLO_TODO_LIST'), 
        'name': title
    }
    r = requests.post('https://api.trello.com/1/Cards', params=payload)


def delete_todo(todo_id):
    payload = {
        'key': os.getenv('TRELLO_KEY'), 
        'token': os.getenv('TRELLO_TOKEN')
    }
    response = requests.delete(f'https://api.trello.com/1/Cards/{todo_id}', params=payload)
    if response.status_code != 200:
        app.logger.error(f"Delete request failed with status code {response.status_code}")

def complete_todo(todo_id):
    payload = {
        'key': os.getenv('TRELLO_KEY'), 
        'token': os.getenv('TRELLO_TOKEN'),
        'idList': os.getenv('TRELLO_COMPLETED_LIST'), 
    }
    response = requests.put(f'https://api.trello.com/1/Cards/{todo_id}', params=payload)

    if response.status_code != 200:
        app.logger.error(f"Delete request failed with status code {response.status_code}")
