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
            self.boards_names_and_ref[boards_ref_data[list_level]['name']] = boards_ref_data[list_level]['id']
            list_level += 1
    
    def get_trello_cards_on_board(self, board_name):
        ref = self.boards_names_and_ref[board_name]
        lists_data_response = requests.get('https://api.trello.com/1/boards/' + ref + '/cards?', params=payload)
        lists_data = json.loads(lists_data_response.content)
        for i, list_name in enumerate(lists_data):
            list_level = i
            self.cards_names_and_ref[lists_data[list_level]['name']] = [lists_data[list_level]['id']]
            list_level += 1

class myTrello(Trello_Data):
    def get_my_board_info(self):
        return self.boards_names_and_ref
    
    def get_my_card_info(self):
        return self.cards_names_and_ref
   

myboards = myTrello()
myboards.get_trello_boards_name_and_ref()
myboards.get_trello_cards_on_board('DevOps Module 2')

print(myboards.get_my_board_info().keys())
#print(myboards.get_my_card_info(5f69d247c5b0c82d14e19438))
boards = myboards.get_my_board_info()
cards = myboards.get_my_card_info()
print(boards)
print(cards)


