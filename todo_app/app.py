from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config

#from todo_app.data.session_items import get_items, add_item, save_item, get_item, remove_item
from todo_app.data.trello_items import Trello_service
from todo_app.data.item import Item

app = Flask(__name__)
app.config.from_object(Config)

service = Trello_service()

@app.route('/')
def index():
    todos = service.get_items()
    sort = request.values.get("sort", "")
    if sort == "asc":
        todos = sorted(todos, key=lambda k: k['status'])
    elif sort == "desc":
        todos = sorted(todos, key=lambda k: k['status'], reverse=True)

    return render_template('index.html', todoList = todos)

@app.route('/new_todo', methods=['POST'])
def add_item_from_form():
    title = request.form['title']
    service.add_item(title)
    return redirect(url_for('index'))

@app.route('/update_todo/<id>', methods=['POST'])
def update_item(id):
    item = service.get_item(id)
    listId = service.get_list_id('Completed')
    
    if request.form.get('completed'):
        item.status= 'Completed'
    else:
        listId = service.get_list_id('Not Started')
        item.status = 'Not Started'
        
    item.listId = listId
    service.save_item(item)
    return redirect(url_for('index'))

@app.route('/remove_todo/<id>', methods=['GET'])
def remove_todo(id):
    service.remove_item(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
