from flask import Flask, redirect, render_template, request

from todo_app.flask_config import Config

from todo_app.data.session_items import get_items, add_item



app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', html_items = items)

@app.route('/', methods = ["POST"])
def new_todo():
    todo = request.form.get("user todo")
    item = add_item(todo)
    return redirect('/')

    