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
        self.lists_with_cards = {}

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
        cards_data_response = requests.get('https://api.trello.com/1/boards/' + ref + '/cards?', params=payload)
        cards_data = json.loads(cards_data_response.content)
        for i, list_name in enumerate(cards_data):
            list_level = i
            self.cards_names_and_ref[cards_data[list_level]['name']] = {'id':[cards_data[list_level]['id']], 'idLIst': [cards_data[list_level]['idList']]}
            list_level += 1
    
    def get_trello_lists_on_board(self, board_name):
        ref = self.boards_names_and_ref[board_name]
        lists_data_response = requests.get('https://api.trello.com/1/boards/' + ref + '/lists?', params=payload)
        list_data = json.loads(lists_data_response.content)
        for i, list_name in enumerate(list_data):
            list_level = i
            self.lists_names_and_ref[list_data[list_level]['name']] = list_data[list_level]['id']
            list_level += 1
    
    def get_trello_cards_on_list(self, list_name):
        ref = self.lists_names_and_ref[list_name]
        lists_data_response = requests.get('https://api.trello.com/1/lists/' + ref + '/cards?', params=payload)
        list_data = json.loads(lists_data_response.content)
        for i, list_name in enumerate(list_data):
            list_level = i
            self.lists_with_cards[list_data[list_level]['name']] = list_data[list_level]['id']
            list_level += 1

class myTrello(Trello_Data):
    def get_my_board_info(self):
        return self.boards_names_and_ref
    def get_my_list_info(self, board_name):
        return self.lists_names_and_ref
    def get_my_card_info(self, board_name):
        return self.cards_names_and_ref

@app.route('/', methods=['GET'])
def index():
    myboards = myTrello()
    myboards.get_trello_boards_name_and_ref()
    boards = list(myboards.get_my_board_info().keys())
    return render_template('Index.html', boards=boards)

@app.route('/board/<board_name>', methods=['POST', 'GET', 'PUT'])
def go_to_board_tasks(board_name):
    myboards = myTrello()
    myboards.get_trello_boards_name_and_ref()
    myboards.get_trello_cards_on_board(board_name)
    myboards.get_trello_lists_on_board(board_name)
    cards = myboards.get_my_card_info(board_name)
    lists = myboards.get_my_list_info(board_name)
    if request.method == 'POST':
       payload_data = payload.copy()
       payload_data['idList'] = request.form['idList']
       payload_data['name'] = request.form['title']
       requests.post('https://api.trello.com/1/cards', params=payload_data)
       return redirect(url_for('index'))
    elif request.method == 'PUT':
       payload_data = payload.copy()
       payload_data['idList'] = request.form['idList']
       payload_data['id'] = request.form['card_name']
       requests.post('https://api.trello.com/1/cards', params=payload_data)
       return redirect(url_for('index'))
    else:   
        return render_template('boardtasks.html', cards=cards, lists=lists)

@app.route('/lists/<board_name>')
def go_to_board_lists(board_name):
    myboards = myTrello()
    myboards.get_trello_boards_name_and_ref()
    myboards.get_trello_lists_on_board(board_name)
    lists = myboards.get_my_list_info(board_name)
    return render_template('my_lists.html', lists=lists)