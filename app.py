
from flask import Flask, render_template, redirect, url_for, request,json
from flask_config import Config
import session_items as session
import requests
import os


app = Flask(__name__)
app.config.from_object(Config)

base_url = "https://api.trello.com/1/"
query = {'key': os.getenv('API_KEY'), 'token': os.getenv('API_TOKEN')}
id = os.getenv('MEMBER_ID')

@app.route('/')
def index():
    to_do = []
    item = {}
    url = base_url + '/boards/' + os.getenv('BOARD_ID') + '/cards'
    response = requests.get(url= url, params = query)
    trello_cards = response.json()
    for card in trello_cards:
        items[card] = trello_cards{'id': id, "Status" : "name" , "Desc" : "desc"}
    return  render_template('index.html',items=items)

@app.route('/items/new', methods=['POST'])
def add_item():
    title = request.form['title']
    session.add_item(title)
    lists = request.form.get('title')
    return redirect("/")

@app.route('/items/<id>/complete')
def complete_item(id):
    session.save_item(id)
    return redirect("/")

if __name__ == '__main__':
    app.run()


 
