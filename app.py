import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, request, redirect, url_for
import session_items as session
load_dotenv()



app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/', methods=['get'])
def index():
    todo_url = 'https://api.trello.com/1/lists/5f637aafcce13f603c570ebd/cards?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN'))
    todo_list = requests.get(todo_url)
    json_data = todo_list.json()
    return render_template('index.html', listall=json_data)

@app.route('/additem', methods=['post'])
def add():
    newItem = request.form.get('new_title')
    session.add_item(newItem)
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run()