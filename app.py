from flask import Flask, redirect, render_template, request, url_for
import trello_cards
import os
from card import Card
from view_model import ViewModel

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_items():
    # trello_todos = trello_cards.get_items()
    items = trello_cards.get_items()

    cards = []
    for item in items:
        card = Card(
            item["id"], 
            item["name"], 
            item["desc"], 
            item["idList"]
        )
        cards.append(card)

    # return render_template('index.html', todos=cards)
    return render_template('index.html', model=ViewModel(items))


@app.route('/', methods=['POST'])
def add_item():
    name = request.form['name']
    desc = request.form['desc']

    trello_cards.add_new_item(name, desc)
    return redirect('/')

@app.route('/done', methods=['GET'])
def get_done_items():
    done = trello_cards.get_done_items()

    return render_template('done.html', dones=done)

@app.route('/done/<id>', methods=['POST'])
def update_item(id):
    trello_cards.update_item(id)

    return redirect('/done')


@app.route('/delete_item/<id>', methods=['POST'])
def delete_item(id):
    trello_cards.delete_item(id)

    # return render_template('index.html')
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
