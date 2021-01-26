import requests
import os

def get_cards_for_board():
    board_id = os.getenv("TRELLO_BOARD_ID")
    key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_API_TOKEN")

    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    params = { "key": key, "token": token }
    response = requests.get(url, params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Wrong status on cards response: {response.status_code}")

def add_todo(name):
    key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_API_TOKEN")
    todo_list_id = os.getenv("TRELLO_TODO_LIST_ID")

    url = f"https://api.trello.com/1/cards/"
    params = { "key": key, "token": token, "idList": todo_list_id, "name": name }
    response = requests.post(url, params)

    if response.status_code == 200:
        return
    else:
        raise Exception(f"Wrong status on cards response: {response.status_code}")

def complete_todo(todo_id):
    key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_API_TOKEN")
    done_list_id = os.getenv("TRELLO_DONE_LIST_ID")

    url = f"https://api.trello.com/1/cards/{todo_id}"
    params = { "key": key, "token": token, "idList": done_list_id }
    response = requests.put(url, params)

    if response.status_code == 200:
        return
    else:
        raise Exception(f"Wrong status on cards response: {response.status_code}")