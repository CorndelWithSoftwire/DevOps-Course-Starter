from flask import Flask
from flask import request,redirect,url_for
from todo_app.flask_config import Config
from flask import render_template
from todo_app.data import session_items
import requests
import os
import json

app = Flask(__name__)
app.config.from_object(Config)

def get_trello_API_credentials():
    f = open("todo_app\Trello_API_Keys.txt", "r").read().split("\n")
    return {'key': f[0], 'token': f[1]}

api_keys = get_trello_API_credentials()
payload = api_keys

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


@app.route('/')
def index():
    boards = get_trello_boards_names()
    return render_template('Index.html', boards=boards)

@app.route('/bt')
def bt():
    cards = get_trello_cards()
    return render_template('boardtasks.html', cards=cards)

@app.route('/<id>')
def task(id):
    item = session_items.get_item(id)
    return render_template('single_item.html', item=item)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        title = (request.form['title'])
        session_items.add_item(title)
        return redirect(url_for('index'))
    else:
        return render_template('add_items.html')

if __name__ == '__main__':
    app.run()
