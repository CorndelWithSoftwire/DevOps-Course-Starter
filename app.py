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
    todo_list = requests.get('https://api.trello.com/1/lists/5f637aafcce13f603c570ebd/cards?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN')))
    todo_json = todo_list.json()

    doing_list = requests.get('https://api.trello.com/1/lists/5f637aaff47bd67c32c891e5/cards?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN')))
    doing_json = doing_list.json()    
     
    done_list = requests.get('https://api.trello.com/1/lists/5f637aaf45a6967f43725861/cards?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN')))
    done_json = done_list.json()

    return render_template('index.html', list_todo=todo_json, list_doing=doing_json, list_done=done_json)

@app.route('/additem', methods=['post'])
def add():
    new_item = request.form.get('new_title')
    add_todo_url = 'https://api.trello.com/1/cards?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN')) + "&idList=5f637aafcce13f603c570ebd" + "&name=" + new_item + "&desc=from Jamies App"
    todo_list = requests.post(add_todo_url)
    return redirect('/', code=302)

@app.route('/movetodone/<id>', methods=['get'])
def move_to_done(id):
    move_to_done_url = 'https://api.trello.com/1/cards/' + id +'?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN')) + "&idList=5f637aaf45a6967f43725861"
    move_list = requests.put(move_to_done_url)
    print(move_list)
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run()