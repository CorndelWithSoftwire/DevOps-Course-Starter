from flask import Flask, render_template, redirect
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items_list = get_items()
    return render_template("index.html", items = items_list)

@app.route('/add_item')
def add():
    hardcoded_item_title = "New Item"
    add_item(hardcoded_item_title)
    return redirect("/")


if __name__ == '__main__':
    app.run()

