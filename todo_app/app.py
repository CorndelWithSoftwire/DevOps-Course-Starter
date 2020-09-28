from flask import Flask, render_template, redirect, url_for, request
from classes import to_do_item
from trello import get_cards, post_item
from todo_app.flask_config import Config
import requests, os

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET'])
def index():
    items = get_cards()
    # app.logger.info('Processing get cards request')
    return render_template('index.html', items = items)

@app.route('/items/new', methods=['POST'])
def add_item():
    api_key = os.getenv('API_KEY')
    api_token = os.getenv('API_TOKEN')
    things_to_do = os.getenv('THINGS_TO_DO')
    params = {'key': api_key, 'token': api_token, 'idList': things_to_do, 'name': request.form['title']}

    response = requests.post(f'https://api.trello.com/1/cards', params=params) 

    return redirect(url_for('index'))


@app.route('/items/<id>/complete')
def complete_item(id):
    api_key = os.getenv('API_KEY')
    api_token = os.getenv('API_TOKEN')
    done = os.getenv('DONE')
    params = {'key': api_key, 'token': api_token, 'idList': done}

    response = requests.put(f'https://api.trello.com/1/cards/{id}', params=params) 

    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()
