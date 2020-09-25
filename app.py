from trello_items import get_cards, get_cards_list
from flask import Flask, render_template, request, redirect, url_for
import requests
import os
import json

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    tasks=[]
    for card in get_cards():
        card_list = get_cards_list(card['id'])
        card['task_status']=card_list['name']
        tasks.append(card)
    
    return render_template('index.html', todos = tasks)

#import session_items as session

if __name__ == "__main__":
    app.run(debug=True)

"""
#update from work 2.0
@app.route('/')
def index():
    items = session.get_items()
    return render_template('index.html', todos = items)
    
@app.route('/add-todo', methods=["POST"])
def add_todo():
    item = request.form.get('todo_task')
    session.add_item(item)
    return redirect('/')

#delete function 
@app.route('/delete-todo', methods=["POST"])
def delete_todo():
    item = request.form.get('todo_id')
    print(item)
    session.delete_item(item)
    return redirect('/')

#update function 
@app.route('/update-todo', methods=["POST"])
def update_todo():
    item = request.form.get('todo_id')
    new_todo_value = request.form.get("title")
    new_status_value = request.form.get("status")
    session.update_item(item, new_todo_value, new_status_value)
    return redirect('/')
    """
