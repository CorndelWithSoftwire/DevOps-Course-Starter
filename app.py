from flask import Flask, redirect, render_template, request, url_for
import trello_cards
import os
from card import Card
from view_model import ViewModel

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def get_items():
        items = trello_cards.get_items()

        cards = []
        for item in items:
            card = Card.from_raw_trello_card(item)
            cards.append(card)

        return render_template('index.html', model=ViewModel(cards))


    @app.route('/', methods=['POST'])
    def add_item():
        name = request.form['name']
        desc = request.form['desc']

        trello_cards.add_new_item(name, desc)
        return redirect('/')
        

    @app.route('/done/<id>', methods=['POST'])
    def update_item(id):
        trello_cards.update_item(id)

        return redirect('/done')


    @app.route('/delete_item/<id>', methods=['POST'])
    def delete_item(id):
        trello_cards.delete_item(id)

        return redirect("/")

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
