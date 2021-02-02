from flask import Flask,render_template, redirect, request

import todo_app.trello_mod as trello

from todo_app.todo_item import TodoItem

app = Flask(__name__)

@app.route('/')

def index():
    raw_trello_cards = trello.get_cards()
    items = [TodoItem.from_raw_trello_card(card) for card in raw_trello_cards]
    return  render_template('index.html',items=items)

@app.route('/item/add', methods=["POST"])
def add_item():
    title = request.form['title']
    trello.add_card(title)
    return redirect('/')

@app.route('/item/<id>/doing')
def move_item_to_doing(id):
    trello.move_card_doing(id)
 #   trello.move_card_done(id)
    return redirect('/')

@app.route('/item/<id>/done')
def move_item_to_done(id):
 #   trello.get_doing_cards(id)
    trello.move_card_done(id)
    return redirect('/')

@app.route('/item/<id>/undo')
def undo_card_move(id):
    trello.undo_card_movement(id)
    return redirect('/')

if __name__ == '__main__':
    app.run()
