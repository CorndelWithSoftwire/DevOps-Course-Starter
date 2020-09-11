from flask import Flask, redirect, render_template, request, url_for
import trello_cards
import session_items as session
import os
from card import Card

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_items():
    trello_todos = session.get_items()

    cards = []
    for trello_todo in trello_todos:
        card = Card(
            trello_todo["id"], 
            trello_todo["name"], 
            trello_todo["desc"], 
            trello_todo["idList"]
        )
        cards.append(card)

    return render_template('index.html', todos=cards)


@app.route('/', methods=['POST'])
def add_item():
    name = request.form['name']
    desc = request.form['desc']

    session.add_new_item(name, desc)
    return redirect('/')

@app.route('/done', methods=['GET'])
def get_done_items():
    done = session.get_done_items()

    return render_template('done.html', dones=done)

@app.route('/done/<id>', methods=['POST'])
def update_item(id):
    session.update_item(id)

    return redirect('/done')


@app.route('/delete_item/<id>', methods=['POST'])
def delete_item(id):
    session.delete_item(id)

    # return render_template('index.html')
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
