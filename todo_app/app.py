from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config
import todo_app.trello_client as trello_client
from todo_app.data.todo_item import TodoItem

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    raw_cards = trello_client.get_cards_for_board()
    todo_items = [TodoItem.from_raw_trello_card(card) for card in raw_cards]
    return render_template('index.html', items_list=todo_items)

@app.route('/add_item', methods=['POST'])
def add_item():
    item_title = request.form['Title']
    add_item(item_title)
    return redirect('/')


if __name__ == '__main__':
    app.run()
