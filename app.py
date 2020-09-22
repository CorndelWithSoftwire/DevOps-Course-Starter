import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, request, redirect, url_for
load_dotenv()

class Todo:
    def __init__(self, item_id, name, status):
        self.item_id = item_id
        self.name = name
        self.status = status

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/', methods=['get'])
def index():
    todo_list_api_response_in_json = requests.get('https://api.trello.com/1/lists/5f637aafcce13f603c570ebd/cards?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN'))).json()
    class_todo_list_api_response = []
    for iteminjson in todo_list_api_response_in_json:
        class_todo_list_api_response.append(Todo(iteminjson['id'],iteminjson['name'], 'To Do'))

    doing_list_api_response_in_json = requests.get('https://api.trello.com/1/lists/5f637aaff47bd67c32c891e5/cards?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN'))).json()    
    class_doing_list_api_response = []
    for iteminjson in doing_list_api_response_in_json:
        class_doing_list_api_response.append(Todo(iteminjson['id'],iteminjson['name'], 'Doing'))
    
    done_list_api_response_in_json = requests.get('https://api.trello.com/1/lists/5f637aaf45a6967f43725861/cards?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN'))).json()
    class_done_list_api_response = []
    for iteminjson in done_list_api_response_in_json:
        class_done_list_api_response.append(Todo(iteminjson['id'],iteminjson['name'], 'Done'))
    

    return render_template('index.html', list_todo=class_todo_list_api_response, list_doing=doing_list_api_response_in_json, list_done=done_list_api_response_in_json)

@app.route('/additem', methods=['post'])
def add():
    new_item = request.form.get('new_title')
    todo_list_api_response = requests.post('https://api.trello.com/1/cards?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN')) + "&idList=5f637aafcce13f603c570ebd" + "&name=" + new_item + "&desc=from Jamies App")
    return redirect('/', code=302)

@app.route('/movetodone/<id>', methods=['get'])
def move_to_done(id):
    move_list = requests.put('https://api.trello.com/1/cards/' + id +'?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN')) + "&idList=5f637aaf45a6967f43725861")
    return redirect('/', code=302)

@app.route('/movetonew/<id>', methods=['get'])
def move_to_new(id):
    move_list = requests.put('https://api.trello.com/1/cards/' + id +'?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN')) + "&idList=5f637aafcce13f603c570ebd")
    return redirect('/', code=302)

@app.route('/movetodoing/<id>', methods=['get'])
def move_to_doing(id):
    move_list = requests.put('https://api.trello.com/1/cards/' + id +'?key=' + str(os.getenv('TRELLO_KEY')) + "&token=" + str(os.getenv('TRELLO_TOKEN')) + "&idList=5f637aaff47bd67c32c891e5")
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run()