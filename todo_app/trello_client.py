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

def add_card(title):
    querystring = {'name': title, 'idList': todo_list_id, 'key': key, 'token': token}
    card_url = f"{base_url}/cards/"
    response = requests.post(url = card_url, params=querystring)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a add card request: {response.status_code}")
def get_card_by_id(id):
    getcard = {'idList': doing_list_id, 'key': key, 'token': token}
    get_card_url = f"{base_url}/cards/{id}"
    response = requests.get(url = get_card_url, params=getcard)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a get card by id request: {response.status_code}")

def move_to_doing_card(id):
    movequery = {'idList': doing_list_id, 'key': key, 'token': token}
    move_url = f"{base_url}/cards/{id}"
    response = requests.put(url= move_url, params = movequery)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a move card by id request: {response.status_code}")


def move_to_done_card(id):
    donequery = {'idList': done_list_id, 'key': key, 'token': token}
    done_url = f"{base_url}/cards/{id}"
    response = requests.put(url= done_url, params = donequery)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a moved card by id request: {response.status_code}")

def undo_done_card(id):
    undoquery = {'idList': todo_list_id, 'key': key, 'token': token}
    undo_url = f"{base_url}/cards/{id}"
    response = requests.put(url= undo_url, params = undoquery)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a undo card by id request: {response.status_code}")