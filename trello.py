from flask import session
from classes import todo_item, todo_status
import os, requests, json

API_PREFIX = 'https://api.trello.com/1/'

API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')
API_PARAMS = {'key': API_KEY, 'token': API_TOKEN}
board = os.getenv('BOARD_ID')

def trello_get(trello_path):
    return requests.get(API_PREFIX + trello_path, params=API_PARAMS.copy()).json()

def get_trello_lists():
    trello_lists = []
    for item in trello_get(f'boards/{board}/lists'):
        list_data = todo_status(
            item['id'],
            item['name']
        )
        trello_lists.append(list_data)
    return trello_lists


def get_trello_cards():
    trello_cards = []
    trello_lists = get_trello_lists()
    for todo_list in trello_lists:
        for item in trello_get(f'lists/{todo_list.trello_id}/cards'):
            todo = todo_item(
                item['id'],
                item['name'],
                item['desc'],
                item['due'],
                todo_list.status
            )
            trello_cards.append(todo)
    return trello_cards

