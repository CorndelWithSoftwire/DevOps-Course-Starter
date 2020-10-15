from flask import Flask, render_template, request
from todo_app.data import session_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    todo_items = session_items.get_items()
    print(todo_items) # adding this line to prove data being pulled from session items 
    return render_template('index.html', items = todo_items)

@app.route('/add', methods=['GET', 'POST'])
def add_item(id,title,status):
    #add_todo_item = session_items.add_item(id, title, status)
    id = request.forms.get('id')
    title = request.forms.get('title')
    status = request.forms.get('status')
    #print = "Item added " + id + " " + title + " " + status + "."
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
