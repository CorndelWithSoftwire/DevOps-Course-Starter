from flask import session
#from classes import todo_item, todo_status
from classes import to_do_item
import os, requests, json

API_PREFIX = 'https://api.trello.com/1/'

API_KEY = os.getenv('API_KEY')
API_TOKEN = os.getenv('API_TOKEN')
API_PARAMS = {'key': API_KEY, 'token': API_TOKEN}
THINGS_TO_DO = os.getenv('THINGS_TO_DO')
DOING = os.getenv('DOING')
DONE = os.getenv('DONE')
board = os.getenv('BOARD_ID')


def get_cards():
    board_id = os.getenv("BOARD_ID")
    api_key = os.getenv("API_KEY")
    api_token = os.getenv("API_TOKEN")
    response = requests.get(f'https://api.trello.com/1/boards/{board_id}/cards', params={'key': api_key, 'token': api_token})
    
    trello_card_lists = response.json()

    our_card_list = []
    for card in trello_card_lists:
        if card["idList"] == THINGS_TO_DO:
            status = "Not Started"
        elif card["idList"] == DOING:
            status = "In Progress"
        else:
            status = "Complete"
    our_card_list.append(to_do_item(card["id"], status, card["name"]))

    return our_card_list


def post_item(title):
    url = API_PREFIX + 'cards'
    post_params = API_PARAMS.copy()
    post_params['idList'] = THINGS_TO_DO('Not Started')
    post_params['name'] = title

    return requests.request(
        "POST", 
        url,
        params=post_params
    )




