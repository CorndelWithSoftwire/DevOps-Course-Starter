from trello_cards import Item
import os
import json
import requests 

def get_auth_params():
    return {    
                'key': os.environ.get('TRELLO_KEY'), 
                'token': os.environ.get('TRELLO_TOKEN') 
            }

def service_url_get_boards():
    return 'https://api.trello.com/1/members/me/boards'

def service_get_list_from_board(boardID):
    return 'https://api.trello.com/1/boards/'+boardID+'/lists'

def service_create_card():
     return 'https://api.trello.com/1/cards'

def service_get_card_of_list(listId):
     return 'http://api.trello.com/1/lists/'+listId+'/cards'

def service_move_card_url(cardId):
     return ('http://api.trello.com/1/cards/%s' % cardId)



def get_all_boards():

    response = requests.request("GET", service_url_get_boards(), params=get_auth_params())
    boards = response.text
    return boards

def get_board_by_name(name):

    boards = json.loads(get_all_boards())
    return next((board for board in boards if board['name'] == name), None)

def get_all_lists():
    url = service_get_list_from_board(os.environ.get('TRELLO_BOARD_ID'))

    response = requests.get(url, params = get_auth_params())
    lists = response.text
    return lists

def get_list_by_name(name):
    lists = json.loads(get_all_lists())
    return next((lister for lister in lists if lister['name'] == name), None)

def add_card_by_name(name):
    todo_list = get_list_by_name('To Do')

    extra_params = { 'name': name, 'idList': todo_list['id'] }
    params = get_auth_params()
    params.update(extra_params)
    url = service_create_card()
    response = requests.post(url, params = params)
    card = response.text
    return Item.trelloCard(json.loads(card), todo_list)

def get_cards_by_list_name(name):
    todo_list = get_list_by_name(name)
    params = get_auth_params()
    url = service_get_card_of_list(todo_list['id'])
    response = requests.post(url, params = params)
    cards = response.text
    return cards


def get_all_cards():
    lists = json.loads(get_all_lists())
    cards = []
    for card_list in lists:
        lists_cards = get_cards_by_list_name(card_list['name'])
        list_card_json = json.loads(lists_cards)
        for card in list_card_json:
            cards.append(Item.trelloCard(card, card_list))
    return cards


def get_card_by_id(id):
    cards = get_all_cards()
    return next((card for card in cards if card['id'] == id), None)


def move_card_to_new_list(card_id, to_list_name):
    to_list=get_list_by_name(to_list_name)
    extra_params = { 'idList': to_list['id'] }
    params = get_auth_params()
    params.update(extra_params)
    url = service_move_card_url(card_id)

    response = requests.put(url, params = params)
    card = response.json()

    return card