from flask import Flask, render_template, request
from todo_app.flask_config import Config
import requests
import os
from todo_app.data.item import Item
import todo_app.data.trello_items as trello_items
from todo_app.data.get_items import ViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
   
    @app.route('/')
    def index():
        response_json = trello_items.get_trello_cards()
        items = []
        item_view_model = ViewModel(items)
        for trello_list in response_json:
            for card in trello_list['cards']:
                item = Item.from_trello_card(card, trello_list)
                items.append(item)
        return render_template('index.html', view_model=item_view_model)
   
    @app.route('/create-todo', methods=['Post'])
    def create_new_todo():
        response = trello_items.create_todo()
        return index()
        
    @app.route('/update_status', methods=['POST'])
    def update_status():
        response = trello_items.change_status()
        return index()
    return app