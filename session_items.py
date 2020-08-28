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
    """
    Fetches all saved items from the trello api.

    Returns:
        list: The list of items.
    """
    
    cards_request = requests.get(base_request_url+'cards'+request_credentials)

    cards_json = json.loads(cards_request.content)
    list_id_dict = get_lists()

    items = []
    for node in cards_json:
        items.append(ToDoItem(node['id'], list_id_dict[node['idList']], node['name']))  
    
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


def add_item(title):
    """
    Adds a new item with the specified title to the board.

    Args:
        title: The title of the item.
    """

    json_list = get_lists()

    todo_list = ''
    for key, value in json_list.items():
        if value == 'Not Started':
            todo_list = key

    url = 'https://api.trello.com/1/cards'+request_credentials+'&idList='+todo_list+'&name='+title

    response = requests.post(url)
    print(response.text)


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
    url = 'https://api.trello.com/1/cards/'+id+request_credentials

    response = requests.delete(url)

    print(response.text)

def get_lists() -> dict:
    json_response = json.loads(requests.get(base_request_url+'lists'+request_credentials).content)
    board_id_dict = {}
    for node in json_response:
        board_id_dict[node['id']] = node['name']
    return board_id_dict    

class ToDoItem(object):
    def __init__(self, id, status, title):
        self.id = id
        self.status = status
        self.title = title

    def __str__(self):
        return self.title+'-'+self.status