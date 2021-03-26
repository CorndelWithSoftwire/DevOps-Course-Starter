
from flask import Flask, render_template, request, redirect, url_for, session
from todo_app.data import session_items

from todo_app.flask_config import Config
from todo_app.trello import Trello
import requests
import os
app = Flask(__name__)
app.config.from_object(Config)
secret_key = os.getenv('SECRET_KEY')

api_key = os.getenv('TRELLO_API_KEY')
api_token = os.getenv('TRELLO_TOKEN')
board_id= os.getenv('TRELLO_BOARD_ID')
listid_todo = os.getenv('ID_LIST_TODO')
listid_doing = os.getenv('ID_LIST_DOING')
listid_done = os.getenv('ID_LIST_DONE')
listid_newlist = os.getenv('ID_LIST_NEWLIST')
cards_cardOne =os.getenv('CARDS_TODO_CARD_ONE')
cards_cardTwo =os.getenv('CARDS_TODO_CARD_TWO')
cards_cardThree =os.getenv('CARDS_TODO_CARD_THREE')
cards_trelloDone =os.getenv('CARDS_TRELLODONE_CARD')
cards_trelloBoard =os.getenv('CARDS_DEVOPSTRELLOBOARD')


trello=Trello()

@app.route('/')
def index():
    
  #Call trello.py get cards from List
    response = trello.getCardsfromList()
    items=[]
    for item in response.json():
        if item['idList'] ==listid_todo:
            status="ToDo"
        elif item['idList'] == listid_done:
            status ='Done'
        items.append({'id':item['id'], 'status':status, 'title': item['name']})
    return render_template('index.html', items=items)





if __name__ == '__main__':
    app.run()
