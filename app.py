from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import requests
import os 

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/')
def index():
    board_id = os.getenv('TRELLO_ID')
    board_key = os.getenv('TRELLO_KEY')
    board_token = os.getenv('TRELLO_TOKEN')
    items_response = requests.get(f'https://api.trello.com/1/boards/{board_id}/cards',params={'key': board_key,'token': board_token})
    return render_template('index.html', items=items)


@app.route('/items', methods=['POST'])
def add_item():
    title = request.form['text-input']
    session.add_item(title)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
