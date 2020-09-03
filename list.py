import requests
import os
from item import Item

class List:
    def __init__(self, id, name, cards={}):
        self.id = id
        self.name = name
        self.cards = cards

    def get_remote_cards(self):
        cards = requests.get(f"https://api.trello.com/1/lists/{self.id}/cards", params={
            'fields': 'name,desc,idList',
            'key':     os.getenv('SECRET_KEY'),
            'token':   os.getenv('SECRET_TOKEN')
        }).json()

        self.cards = { c['id'] : Item(c['name'], c['desc'], self.id, c['id']) for c in cards}

    def add_card(self, card):
        self.cards[card.id] = card

    def get_card(self, id):
        return self.cards[id]