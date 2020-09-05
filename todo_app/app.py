from flask import Flask, request, render_template
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html',items=items)

@app.route('/add_todo_item', methods=['POST']) 
def add_todo_item(): 
    new_todo_item = request.form.get('newitem', "")
    items = add_item(new_todo_item)
    items = get_items()
    return render_template('index.html',items=items)

if __name__ == '__main__':
    app.run()
