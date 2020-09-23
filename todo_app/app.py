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
    f = open("todo_app/Trello_API_Keys.txt", "r").read().split("\n")
    return {'api_key': f[0], 'api_token': f[1]}


@app.route('/')
def index():
    items = session_items.get_items()
    return render_template('Index.html', items=items)

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
