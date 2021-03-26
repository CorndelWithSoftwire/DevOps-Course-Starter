from flask import Flask, render_template, request, redirect, url_for
from todo_app.data import session_items

from todo_app.flask_config import Config
import requests
import os


app = Flask(__name__)
app.config.from_object(Config)

api_key = os.getenv('TRELLO_API_KEY')
api_token = os.getenv('TRELLO_TOKEN')
board_id= os.getenv('TRELLO_BOARD_ID')
params= {'key': api_key, 'token': api_token}

all_boards = client.list_boards()
my_board = all_boards[0]
my_lists = my_board.list_lists()

@app.route('/')
def get_todo_item():
    to_do = []
    for card in my_lists:
        cards = card.list_cards()
        if card.closed == False:
            for i in cards:
                to_do.append(i.name)
    return to_do[random.randint(0, len(to_do)-1)]






if __name__ == "__main__":
    app.run(debug=True)