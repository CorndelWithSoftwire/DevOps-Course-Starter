from flask import Flask, render_template, request, redirect, url_for
import config as cf
from model import Item

import session_items as session
import requests
import json


app = Flask(__name__)
app.config.from_object('flask_config.Config')
#load_dotenv()

@app.route('/')
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
        if card['idList'] == '5f5a4b008a129438843fcf10':
            status = 'To Do'
        else:
            status = 'Done'

        item = Item(card['id'], status, card['name'])
        items_list.append(item)

    return render_template('index.html', items=items_list)


if __name__ == '__main__':
    app.run()


"""
Add a complete_item route that accepts the ID of an item as a
parameter and then calls a method to change its status from 'To
Do' to 'Done'
curl -i "localhost:5000/api/foo?a=hello&b=world" 
"""
@app.route('/complete_item/<idCard>', methods=['PUT'])
def update_card(idCard):

    add_card_to_done()

    url = "https://api.trello.com/1/cards/{idCard}"
    headers = {"Accept": "application/json"}
    query = cf.get_trello_query()
    #No obvious way of retrieving the done List Id, 
    #therefore reusing/mocking the example one instead 
    query['idList'] = '5abbe4b7ddc1b351ef961415'
    response = requests.request( "PUT", url, headers=headers, params=query )
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


#create card/item
@app.route('/add', methods=['POST'])
def add_card():
    url = "https://api.trello.com/1/cards"
    
    list_id = cf.get_trello_list_id()
    query = cf.get_trello_query()
    #No obvious way of retrieving the created List Id, 
    #therefore reusing/mocking the example one instead 
    query['idList'] = list_id
    response = requests.request("POST", url, params=query )
    #print(response.text)
    return redirect(url_for('index'))


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
def create_to_do_board():

    url = "https://api.trello.com/1/boards/"
    query = cf.get_trello_query()
    query['name'] = 'MyCorndelDevOpsToDoBoard'
    
    response = requests.request(  "POST", url, params=query )
    print(response.text)

