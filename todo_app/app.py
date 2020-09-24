from flask import Flask, render_template, redirect
from classes import to_do_item
# from trello import trello_get, get_trello_lists, get_trello_cards
from trello import get_cards
from todo_app.flask_config import Config
import requests

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET'])
def index():
    items = get_cards()
    app.logger.info('Processing get cards request')
    return render_template('index.html', items = items)

@app.route('/create', methods=['POST'])
def new_todo():
    trello_post(request.form['add_todo'])
    return redirect('/')

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()
