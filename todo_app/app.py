from flask import request,redirect,url_for,Response,Flask,render_template
from todo_app.flask_config import Config
from todo_app.data import session_items
import requests
import os
import json

app = Flask(__name__)
app.config.from_object(Config)

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
        boards_data_response = requests.get('https://api.trello.com/1/members/me/boards?', params=payload)
        boards_data = json.loads(boards_data_response.content)
        for i, board in enumerate(boards_data):
            list_level = i
            self.boards_names_and_ref[boards_data[list_level]['name']] = boards_data[list_level]['id']
            list_level += 1
    
    def get_trello_cards_on_board(self, board_name):
        ref = self.boards_names_and_ref[board_name]
        lists_data_response = requests.get('https://api.trello.com/1/boards/' + ref + '/cards?', params=payload)
        lists_data = json.loads(lists_data_response.content)
        for i, list_name in enumerate(lists_data):
            list_level = i
            self.cards_names_and_ref[lists_data[list_level]['name']] = [lists_data[list_level]['id']]
            list_level += 1
    
    def get_trello_lists_on_board(self, board_name):
        ref = self.boards_names_and_ref[board_name]
        lists_data_response = requests.get('https://api.trello.com/1/boards/' + ref + '/lists?', params=payload)
        list_data = json.loads(lists_data_response.content)
        for i, list_name in enumerate(list_data):
            list_level = i
            self.lists_names_and_ref[list_data[list_level]['name']] = list_data[list_level]['id']
            list_level += 1

class myTrello(Trello_Data):
    def get_my_board_info(self):
        return self.boards_names_and_ref
    def get_my_list_info(self, board_name):
        return self.lists_names_and_ref
    def get_my_card_info(self, board_name):
        return self.cards_names_and_ref
   

myboards = myTrello()
myboards.get_trello_boards_name_and_ref()
myboards.get_trello_cards_on_board('DevOps Module 2')
myboards.get_trello_lists_on_board('DevOps Module 2')
#myboards.get_trello_cards_on_list()

@app.route('/')
def index():
    myboards = myTrello()
    myboards.get_trello_boards_name_and_ref()
    myboards.get_trello_cards_on_board('DevOps Module 2')
    myboards.get_trello_lists_on_board('DevOps Module 2')
    boards = list(myboards.get_my_board_info().keys())
    return render_template('Index.html', boards=boards)

@app.route('/board/<board_name>')
def go_to_board_tasks(board_name):
    myboards = myTrello()
    myboards.get_trello_boards_name_and_ref()
    myboards.get_trello_cards_on_board('DevOps Module 2')
    myboards.get_trello_lists_on_board('DevOps Module 2')
    cards = myboards.get_my_card_info(board_name)
    return render_template('boardtasks.html', cards=cards)

@app.route('/lists/<board_name>')
def go_to_board_lists(board_name):
    myboards = myTrello()
    myboards.get_trello_boards_name_and_ref()
    myboards.get_trello_cards_on_board('DevOps Module 2')
    myboards.get_trello_lists_on_board('DevOps Module 2')
    lists = myboards.get_my_list_info(board_name)
    return render_template('my_lists.html', lists=lists)

@app.route('/add', methods=['POST', 'GET'])
def add():
    myboards = myTrello()
    myboards.get_trello_boards_name_and_ref()
    myboards.get_trello_cards_on_board('DevOps Module 2')
    myboards.get_trello_lists_on_board('DevOps Module 2')
    if request.method == 'POST':
       payload_data = payload.copy()
       payload_data['idList'] = request.form['idList']
       payload_data['name'] = request.form['title']
       requests.post('https://api.trello.com/1/cards', params=payload_data)
       return redirect(url_for('index'))
    else:
       lists = myboards.get_my_list_info('name')
       return render_template('add_items.html', lists=lists)

#@app.route('/<id>')
#def task(id):
#    item = session_items.get_item(id)
#    return render_template('single_item.html', item=item)



#if __name__ == '__main__':
#    app.run()

"""
def get_trello_boards_reference():
    boards_ref_data_response = requests.get('https://api.trello.com/1/members/me/boards?', params=payload)
    boards_ref_data = json.loads(boards_ref_data_response.content)
    board_ref_list = [item ['shortLink'] for item in boards_ref_data]
    return board_ref_list

def get_trello_boards_names():
    boards_ref_data_response = requests.get('https://api.trello.com/1/members/me/boards?', params=payload)
    boards_ref_data = json.loads(boards_ref_data_response.content)
    board_name_list = [item ['name'] for item in boards_ref_data]
    return board_name_list

def get_trello_lists_names():
    boards = get_trello_boards_reference()
    lists_name = []
    for ref in boards:
        ref = ref
        lists_data_response = requests.get('https://api.trello.com/1/boards/' + ref + '/lists?', params=payload)
        lists_data = json.loads(lists_data_response.content)
        lists_name.append([list_name ['name'] for list_name in lists_data])
    return lists_name

def get_trello_lists_reference():
    boards = get_trello_boards_reference()
    lists_ref = []
    for ref in boards:
        ref = ref
        lists_data_response = requests.get('https://api.trello.com/1/boards/' + ref + '/lists?', params=payload)
        lists_data = json.loads(lists_data_response.content)
        lists_ref.append([list_name['id'] for list_name in lists_data])
    return lists_ref

def get_trello_cards():
    cards = get_trello_boards_reference()
    card_name = []
    for card in cards:
        ref = card
        card_data_response = requests.get('https://api.trello.com/1/boards/' + ref + '/cards?', params=payload)
        card_data = json.loads(card_data_response.content)
        card_name.append([card ['name'] for card in card_data])
    return card_name
"""


