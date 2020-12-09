import os
import requests

from todo_item import TodoItem

board_id = os.getenv('TRELLO_BOARD_ID')
api_key = os.getenv('TRELLO_API_KEY')
api_secret = os.getenv('TRELLO_API_SECRET')
not_started = os.getenv('NOT_STARTED')

def get_cards():
    response = requests.get(f'http://api.trello.com/1/boards/{board_id}/cards', params ={'key': api_key, 'token': api_secret, 'idList': '5f523f68b6899286325cf067'})
    return response.json()

def get_cards_list(card_id):
    response = requests.get(f'https://api.trello.com/1/cards/{card_id}/list', params ={'key': api_key, 'token': api_secret})
    return response.json()

def get_lists():
    response = requests.get(f'http://api.trello.com/1/boards/{board_id}/lists', params ={'key': api_key, 'token': api_secret})
    return response.json()

def create_task(new_task_text):
    query={'key': api_key, 'token': api_secret, 'idList': not_started, 'name': new_task_text}
    response = requests.request(
        "POST",
        f"https://api.trello.com/1/cards",
        params=query
    )
    return response

def delete_todo(id):
    
    response = requests.delete(
        f"https://api.trello.com/1/cards/{id}", params ={'key': api_key, 'token': api_secret}
    )

    print(response.text)
    return response.json()
