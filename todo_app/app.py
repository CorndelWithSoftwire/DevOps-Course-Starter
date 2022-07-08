from flask import Flask, render_template, url_for, redirect, request
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template("index.html", items=items)


@app.route('/add_items', methods=["POST"])
def create_items():
    new_item = request.form.get('todo')
    add_item(new_item)
    return redirect("/")

