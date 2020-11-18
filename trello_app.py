from flask import Blueprint
from flask import current_app as app
from flask import Flask, render_template, request, redirect, url_for
import config as cf
from model import Item, ViewModel

import session_items as session
import requests
import json

trello_bp = Blueprint( 'trello_bp', __name__)

@trello_bp.route('/', methods=['GET'])
#@app.route('/')
def index():
    board_id = cf.get_trello_board_id()
    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    query = cf.get_trello_query()
    
    response = requests.request(
        "GET",
        url,
        params=query
        )
    
    cards = json.loads(response.text)
    items_list = list()
    for card in cards:
        status = 'To Do' 
        if card['idList'] == cf.get_trello_list_id():
            status = 'To Do'
        elif card['idList'] == cf.get_trello_list_id_doing():
            status = 'Doing'
        else:
            status = 'Done'

        item = Item(card['id'], status, card['name'], card['dateLastActivity'])
        items_list.append(item)

    item_view_model = ViewModel(items_list)
    #render_template('index.html', view_model=item_view_model)

    #return render_template('index.html', items=items_list)
    return render_template('index.html', view_model=item_view_model)


@trello_bp.route('/complete_item/<idCard>', methods=['GET', 'PUT', 'POST'])
#@app.route('/complete_item/<idCard>', methods=['GET', 'PUT'])
def update_card(idCard):

    url = f"https://api.trello.com/1/cards/{idCard}"
    headers = {"Accept": "application/json"}
    list_id = cf.get_trello_list_id_done()
    query = cf.get_trello_query()
    query['idList'] = list_id
    response = requests.request( "PUT", url, headers=headers, params=query )
    return redirect(url_for('trello_bp.index'))


@trello_bp.route('/add', methods=['POST'])
#@app.route('/add', methods=['POST'])
def add_card():
    url = "https://api.trello.com/1/cards"
    
    list_id = cf.get_trello_list_id()
    query = cf.get_trello_query()
    
    query['idList'] = list_id
    if request.form['title']:
        query['name'] = request.form['title']

    response = requests.request("POST", url, params=query )
    return redirect(url_for('trello_bp.index'))


def add_card_to_todo():
        add_card()


def add_card_to_done():
    add_card()


#delete card/item
def remove_card(id):
    url = f"https://api.trello.com/1/cards/{id}"
    response = requests.request("DELETE", url )
    print(response.text)


#Fetch Cards on a list
def get_cards(id):
    url = f"https://api.trello.com/1/lists/{id}/cards"
    
    query = cf.get_trello_query()    
    response = requests.request("GET", url, params=query)
    print(response.text)


# create lists
def add_list_to_board(name):
    url = "https://api.trello.com/1/lists"
    query = cf.get_trello_query()
    
    #query['name'] = 'MyCorndelDevOpsToDoBoard'
    query['name'] = name
    query['idBoard'] = '5abbe4b7ddc1b351ef961414'

    response = requests.request( "POST", url, params=query )
    print(response.text)


#Create New Board
def create_to_do_board(board_name = 'MyCorndelDevOpsToDoBoard'):

    url = "https://api.trello.com/1/boards/"
    query = cf.get_trello_query()
    query['name'] = board_name
    
    response = requests.request(  "POST", url, params=query )
    print(response.text)