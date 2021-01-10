
from flask import current_app
import requests
from requests.exceptions import HTTPError
import json


class Trello:
    def __init__(self, current_app):
        self.board = current_app.config['TRELLO_BOARD']
        self.url_prefix = "https://api.trello.com/1/"
        self.query = {
            'key': current_app.config['TRELLO_KEY'],
            'token': current_app.config['TRELLO_TOKEN']
        }

    def get_lists(self):
        """
        Gets the lists associated with the board
        Returns:
            dictionary of lists
        """
        url = self.url_prefix+"boards/"+self.board+"/lists"
        response = requests.get(url, params=self.query)
        response.raise_for_status()
        return response.json()

    def get_cards(self):
        """
        Gets the cards associated with the board
        Returns:
            dictionary of the cards on the board
        """
        url = self.url_prefix+"boards/"+self.board+"/cards"
        response = requests.get(url, params=self.query)
        response.raise_for_status()
        return response.json()

    def get_card(self, id):
        """
        Fetches the saved item with the specified ID.
        Args:
            id: The ID of the card.
        Returns:
            card: The saved card
        """
        url = self.url_prefix+"cards/"+id
        response = requests.get(url, params=self.query)
        response.raise_for_status()
        return response.json()

    def add_card(self, Lists, name, desc, due):
        """
        Adds a new item with the specified title to the session.
        Args:
            title: The title of the item.
        Returns:
            item: The saved item.
        """
        url = self.url_prefix+"cards"
        query = self.query
        query["name"] = name
        query["idList"] = Lists[0].id
        query["due"] = due
        query["desc"] = desc
        response = requests.post(url, params=query)
        response.raise_for_status()

    def save_card(self, id, name, desc, due, idList):
        """
        Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.
        Args:
            item: The item to save.
        """
        url = self.url_prefix+"cards/"+id
        query = self.query
        query["name"] = name
        query["idList"] = idList
        query["desc"] = desc
        query["due"] = due
        response = requests.put(url, params=query)
        response.raise_for_status()

    def delete_card(self, id):
        """
        Deletes an existing item in the session.
        Args:
            item: the item to delete
        """
        url = self.url_prefix+"cards/"+id
        response = requests.delete(url, params=self.query)
        response.raise_for_status()
