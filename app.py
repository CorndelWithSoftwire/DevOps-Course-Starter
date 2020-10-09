from flask import Flask, redirect, render_template, request, url_for
import trello_cards
import os
from card import Card
from view_model import ViewModel

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_items():
    items = trello_cards.get_items()

    cards = []
    for item in items:
        card = Card.from_raw_trello_card(item)
        cards.append(card)

    return render_template('index.html', model=ViewModel(items))


@app.route('/', methods=['POST'])
def add_item():
    name = request.form['name']
    desc = request.form['desc']

    trello_cards.add_new_item(name, desc)
    return redirect('/')


@app.route('/todo', methods=['GET'])
def get_todo_items():
    todo = trello_cards.get_todo_items()

    return render_template('todo.html', todos=todo)
    

@app.route('/doing', methods=['GET'])
def get_doing_items():
    doing = trello_cards.get_doing_items()

    return render_template('doing.html', doings=doing)


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

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
