import requests
import os
import json

def get_trello_API_credentials():
    f = open("todo_app/Trello_API_Keys.txt", "r").read().split("\n")
    return {'key': f[0], 'token': f[1]}

api_keys = get_trello_API_credentials()
payload = api_keys

class Trello_Data:
    def __init__(self):
        self.boards_names_and_ref = {}
        self.lists_names_and_ref = {}
        self.cards_names_and_ref = {}

    def get_trello_boards_name_and_ref(self):
        list_level = 0
        boards_ref_data_response = requests.get('https://api.trello.com/1/members/me/boards?', params=payload)
        boards_ref_data = json.loads(boards_ref_data_response.content)
        for i, board in enumerate(boards_ref_data):
            list_level = i
            self.boards_names_and_ref[boards_ref_data[list_level]['name']] = boards_ref_data[list_level]['shortLink']
            list_level += 1

class myTrello(Trello_Data):
    def get_my_board_info(self):
        return self.boards_names_and_ref
   

myboards = myTrello()
myboards.get_trello_boards_name_and_ref()

print(myboards.get_my_board_info().keys())
boards = list(myboards.get_my_board_info().keys())
print(boards)
def get_trello_boards_names():
    boards_ref_data_response = requests.get('https://api.trello.com/1/members/me/boards?', params=payload)
    boards_ref_data = json.loads(boards_ref_data_response.content)
    board_name_list = [item ['name'] for item in boards_ref_data]
    return board_name_list

def get_trello_lists_reference():
    boards = get_trello_boards_reference()
    lists_ref = []
    for board in boards:
        board = board
        lists_data_response = requests.get('https://api.trello.com/1/boards/' + board + '/lists?', params=payload)
        lists_data = json.loads(lists_data_response.content)
        lists_ref.append([list_name['id'] for list_name in lists_data])
    return lists_ref

def get_trello_lists_names():
    boards = get_trello_boards_reference()
    lists_name = []
    for listn in boards:
        listn = listn
        lists_data_response = requests.get('https://api.trello.com/1/boards/' + listn + '/lists?', params=payload)
        lists_data = json.loads(lists_data_response.content)
        lists_name.append([list_name['name'] for list_name in lists_data])
    return lists_name

def get_trello_cards():
    cards = get_trello_lists_reference()
    card_name = []
    for card in cards:
        card = card
        card_data_response = requests.get('https://api.trello.com/1/lists/' + card + '/cards?', params=payload)
        card_data = json.loads(card_data_response.content)
        card_name.append([card ['name'] for card in card_data])
    return card_name


myboard_names = get_trello_boards_names()
myboard_ids = get_trello_boards_reference()
mylist_names = get_trello_lists_names()
mylist_ids = get_trello_lists_reference()
mycard_names = get_trello_cards()

print(mycard_names)


