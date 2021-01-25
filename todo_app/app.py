# SETUP INFO - this it the one

from flask import Flask, render_template, request, redirect, url_for
import requests                     # Import the whole of requests
import json
import os        # Secrets for example Trello tokens etc in here (local only)
from todo_app.models.view_model import ViewModel
from todo_app.todo import Todo
app = Flask(__name__)
print ("Program starting now") 

#Set up variables we'll be using

trellokey=os.environ["key"]            # get the secret key
trellotoken=os.environ["token"]         # get the secret token
listid=os.environ["todo_listid"]
cardsurl = "https://api.trello.com/1/cards"

@app.route('/', methods = ["GET","PUT"])
def index():
    thislist=[]                  
    superlist=[] 
    cardsurl = "https://api.trello.com/1/cards"      
    boardurl = f"https://api.trello.com/1/boards/{os.environ['board_id']}/cards"             # The board ID is not a secret!

# Trello GET for recieving all the cards here

    query = {
        'key': trellokey,
        'token': trellotoken                
    }
    board_response = requests.request(                     
         "GET",
         boardurl,
         params=query
     )

    card_list = json.loads(board_response.text)     # A list of cards
    
    for trello_card in card_list:
        todo = Todo.from_trello_card(trello_card)
        superlist.append(todo)

    item_view_model = ViewModel(superlist)
    
    return render_template('index.html', view_model=item_view_model)


@app.route('/addentry', methods = ["POST"])
def entry():
    query = {
        'key': trellokey,
        'token': trellotoken,
        'idList': listid,
        'name': request.form['title']
    }

    response = requests.post(
        cardsurl,
        params=query
    )
    return redirect("/")

@app.route('/complete_item', methods = ["PUT","GET","POST"])

def complete_item():
    done_listid = "5f3528981725711087e10339"
    id = request.form['item_id']
    query = {
        'key': trellokey,
        'token': trellotoken,
        'idList' : done_listid   
    }
    response = requests.request(
        "PUT",
        "https://api.trello.com/1/cards/" + id,
        params=query
    )
    return redirect("/")


if __name__ == '__main__':
   
   app.run()
