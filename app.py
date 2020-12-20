
from flask import Flask, render_template, redirect, url_for, request,json
from flask_config import Config
import requests
import os
import trello_client as trello
from todo_item import TodoItem

app = Flask(__name__)
app.config.from_object(Config)

base_url = "https://api.trello.com/1/"
query = {'key': os.getenv('API_KEY'), 'token': os.getenv('API_TOKEN')}
id = os.getenv('MEMBER_ID')

@app.route('/')
def index():
    raw_trello_cards = trello.get_cards()
    items = [TodoItem.from_raw_trello_card(card) for card in raw_trello_cards]
    return  render_template('index.html',items=items)

@app.route('/items/new', methods=['POST'])
def add_item():
    name = request.form['title']
    trello.add_card(name)
    return redirect("/")

@app.route('/items/<id>/complete')
def complete_item(id):
    trello.move_to_do_card(id)
    return redirect("/")

if __name__ == '__main__':
    app.run()


 
