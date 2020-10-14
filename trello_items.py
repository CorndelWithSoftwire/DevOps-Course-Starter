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

def get_lists():
    response = requests.get(f'http://api.trello.com/1/boards/{board_id}/lists', params ={'key': api_key, 'token': api_secret})
    return response.json()

def create_task(new_task_text):
    for task_list in get_lists():
        print(task_list)
        if task_list['name'] == "Not Started":
            new_task = task_list['id']
    response = requests.post(f'http://api.trello.com/1/cards', params ={'key': api_key, 'token': api_secret, 'idList': new_task, 'name': new_task_text})
    return response.json()


#def update_cards_to_complete(card_id)
 #   requests.put('')