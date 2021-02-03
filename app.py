import trello_items
from todo_item import TodoItem
from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import os
import json

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    tasks=[]
    for card in trello_items.get_cards():
        tasks.append(TodoItem.from_trello_card(card))
    
    return render_template('index.html', todos = tasks)

if __name__ == "__main__":
    app.run(debug=True)

#add-todo
@app.route('/create_task', methods=["POST"])
def add_todo():
    item = request.form.get('todo_task')
    print(item)
    trello_items.create_task(item)
    return redirect('/')


#delete function 
@app.route('/delete_todo', methods=["POST"])
def delete_todo():
    item = request.form.get('todo_id')
    print(item)
    trello_items.delete_todo(item)
    return redirect('/')

#update function 
@app.route('/update_todo', methods=["POST"])
def update_todo():
    id = request.form.get('todo_id')
    new_todo_value = request.form.get("title")
    new_status_value = request.form.get("status")
    lists = trello_items.get_lists()
            
    for task_list in lists:
        if task_list['name']== new_status_value:
            new_list_id = task_list['id']

    print(id)
    print(new_todo_value)
    print(new_status_value)
    print(new_list_id)
    trello_items.update_todo(id, new_todo_value, new_list_id)
    flash("updated")
    return redirect('/')

