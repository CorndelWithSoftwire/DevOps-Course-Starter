import os
import requests

base_url = "https://api.trello.com/1"
board_id = os.getenv('BOARD_ID')
key = os.getenv('API_KEY')
token = os.getenv('API_TOKEN')
todo_list_id = os.getenv('TODO_LIST_ID')
doing_list_id = os.getenv('DOING_LIST_ID')
done_list_id = os.getenv('DONE_LIST_ID')


def get_cards():

    url = f"{base_url}/boards/{board_id}/cards"
    query = {'key': key, 'token': token}
    response = requests.get(url= url, params = query)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a get cards request: {response.status_code}")
    return response.json()

def add_card(name):

    url = f"{base_url}/cards"
    query = {'key': key, 'token': token,'idList':todo_list_id, 'name':name}
    response = requests.post(url= url, params = query)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a add cards request: {response.status_code}")
    
def get_doing_cards(id):

    url = f"{base_url}/cards/{id}"
    query = {'key': key, 'token': token, 'idList':doing_list_id, 'idBoard':board_id}
    response = requests.get(url= url, params = query)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a get cards request: {response.status_code}")
    return response.json(id)

def move_card_doing(id):

    url = f"{base_url}/cards/{id}"
    query = {'key': key, 'token': token,'idList':doing_list_id, 'idBoard':board_id}
    response = requests.put(url= url, params = query)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a move cards request: {response.status_code}")


def move_card_done(id):

    url = f"{base_url}/cards/{id}"
    query = {'key': key, 'token': token,'idList':done_list_id, 'idBoard':board_id}
    response = requests.put(url= url, params = query)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a move cards request: {response.status_code}")

def undo_card_movement(id):

    url = f"{base_url}/cards/{id}"
    query = {'key': key, 'token': token,'idList':doing_list_id, 'idBoard':board_id}
    response = requests.put(url= url, params = query)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a move cards request: {response.status_code}")
