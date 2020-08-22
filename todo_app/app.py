from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config

from todo_app.data.session_items import get_items, add_item, save_item, get_item, remove_item

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', todoList = get_items())

@app.route('/new_todo', methods=['POST'])
def add_item_from_form():
    title = request.form['title']
    add_item(title)
    return redirect(url_for('index'))

@app.route('/update_todo/<id>', methods=['POST'])
def update_item(id):
    ticked = False
    try:
        if request.form['completed'] == 'on':
            ticked = True 
    finally:
        item = get_item(id)
        if ticked:
            item['status'] = 'Completed'
        else:
            item['status'] = 'Not Started'
        save_item(item)
        return redirect(url_for('index'))

@app.route('/sort_status', methods=['GET'])
def sort_statutes():
    todos = get_items()
    newlist = sorted(todos, key=lambda k: k['status'])
    return render_template('index.html', todoList = newlist)

@app.route('/remove_todo/<id>', methods=['GET'])
def remove_todo(id):
    remove_item(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
