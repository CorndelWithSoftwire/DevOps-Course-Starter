# from flask import session
import requests
import logging
import os
import json

logging.basicConfig(level=logging.DEBUG)
_DEFAULT_ITEMS = [
    {'id': 1, 'status': 'Not Started', 'title': 'List saved todo items'},
    {'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added'}
]
boardId = os.environ.get('boardId')
key = os.environ.get('key')
token = os.environ.get('token')

base_request_url = 'https://api.trello.com/1/boards/'+boardId+'/'
request_credentials = '?key='+key+'&token='+token

def get_items() -> list:
    
    cards_request = requests.get(base_request_url+'cards'+request_credentials)
    lists_request = requests.get(base_request_url+'lists'+request_credentials)

    cards_json = json.loads(cards_request.content)
    lists_json = json.loads(lists_request.content)

    board_id_dict = {}
    for node in lists_json:
        board_id_dict[node['id']] = node['name']

    items = []
    for node in cards_json:
        items.append(ToDoItem(node['id'], board_id_dict[node['idList']], node['name']))
        print(node)

    for item in items:
        print(str(item))   
    
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    return items

def get_item(id) -> dict:
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title) -> dict:
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    # id = items[-1]['id'] + 1 if items else 0

    # item = {'id': id, 'title': title, 'status': 'Not Started'}

    # # Add the item to the list
    # items.append(item)
    # session['items'] = items

    # return item


def save_item(item) -> dict:
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    # existing_items = get_items()
    # updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    # session['items'] = updated_items

    # return item


def delete_item_by_id(id) -> None:
    """
    Deletes the item provided. Does nothing if the item does not exist.

    Args:
        item: The item to delete.
    """
    # current_items = session['items']

    # item_to_delete = get_item(id)
    # current_items.remove(item_to_delete)

    # session['items'] = current_items

class ToDoItem(object):
    def __init__(self, id, status, title):
        self.id = id
        self.status = status
        self.title = title

    def __str__(self):
        return self.title+'-'+self.status