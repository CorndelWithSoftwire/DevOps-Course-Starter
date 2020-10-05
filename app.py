from flask import Flask, render_template, request, redirect, url_for
import requests
import os 
from card import Card

app = Flask(__name__)


@app.route('/')
def index():
    board_id = os.getenv('TRELLO_BOARD_ID')
    board_key = os.getenv('TRELLO_KEY')
    board_token = os.getenv('TRELLO_TOKEN')
    items_response = requests.get(f'https://api.trello.com/1/boards/{board_id}/cards',params={'key': board_key,'token': board_token})
    items_dictionary = items_response.json()
    cards = []
    for item in items_dictionary:
        new_card = Card(item["id"], item["name"], item["idList"])
        cards.append(new_card)

    return render_template('index.html', items=cards)


# @app.route('/items', methods=['POST'])
# def add_item():
#     title = request.form['text-input']
#     session.add_item(title)
#     return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
