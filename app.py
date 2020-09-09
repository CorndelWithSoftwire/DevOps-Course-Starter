# SETUP INFO - this it the one

from flask import Flask, render_template, request, redirect, url_for
import requests                     # Import the whole of requests
import json
import session_items as session
import os        # Secrets for example Trello tokens etc in here (local only)
app = Flask(__name__)
app.config.from_object('flask_config.Config')

#Set up variables we'll be using

trellokey=os.environ["key"]            # get the secret key
trellotoken=os.environ["token"]         # get the secret token
@app.route('/', methods = ["GET","PUT"])

def index():
    Items=session.get_items()
    thislist=[]                  
    superlist=[] 
    cardsurl = "https://api.trello.com/1/cards"      
    boardurl = "https://api.trello.com/1/boards/5f3528983d4fb244aae9f934/cards"             # The board ID is not a secret!
    listid = "5f352898dc8a8c31a0a1e439"                         
    # donelistid = "5f3528981725711087e10339"

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

    the_list = json.loads(board_response.text)     # A list of cards
    for todo in the_list:
       
        superlist.append({'name': todo['name'], 'id': todo['id']})

    return render_template('index.html',passedItems=Items,todisplay=superlist)

@app.route('/addentry', methods = ["POST"])
def entry():
    query = {
        'key': trellokey,
        'token': trellotoken,
        'idList': listid,
        'name': request.form['title']
    }

    response = requests.request(
        "POST",
        cardsurl,
        params=query
    )
    return redirect("/")

@app.route('/complete_item', methods = ["PUT","GET","POST"])

def complete_item():
    donelistid = "5f3528981725711087e10339"
    id = request.form['item_id']
    query = {
        'key': trellokey,
        'token': trellotoken,
        'idList' : donelistid   
    }
    response = requests.request(
        "PUT",
        "https://api.trello.com/1/cards/" + id,
        params=query
    )
    return redirect("/")


if __name__ == '__main__':
   
   app.run()
