
from flask import session
import requests
from requests.exceptions import HTTPError
from datetime import datetime
import json

from todo_app.flask_config import Config


class Trello:
    def __init__(self, Config):
        self.board = Config.TRELLO_BOARD
        self.url_prefix = "https://api.trello.com/1/"
        self.query = {
            'key': Config.TRELLO_KEY,
            'token': Config.TRELLO_TOKEN
        }

    def get_lists(self):
        """
        Gets the lists associated with the board
        Returns:
            dictionary of lists
        """
        url = self.url_prefix+"boards/"+self.board+"/lists"
        response = requests.request("GET", url, params=self.query)
        response.raise_for_status()
        return response.json()

    def get_cards(self):
        """
        Gets the cards associated with the board
        Returns:
            dictionary of the cards on the board
        """
        url = self.url_prefix+"boards/"+self.board+"/cards"
        response = requests.request("GET", url, params=self.query)
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
        response = requests.request("GET", url, params=self.query)
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
        response = requests.request("POST", url, params=query)
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
        response = requests.request("PUT", url, params=query)
        response.raise_for_status()

    def delete_card(self, id):
        """
        Deletes an existing item in the session.
        Args:
            item: the item to delete
        """
        url = self.url_prefix+"cards/"+id
        response = requests.request("DELETE", url, params=self.query)
        response.raise_for_status()


class Card:
    """
    card class for processing contents of API
    Returns:
        Card class object
    """

    def __init__(self, Lists, i):
        self.id = i["id"]
        self.name = i["name"]
        self.listId = i["idList"]
        self.desc = i["desc"]
        self.creationTime = datetime.fromtimestamp(int(i["id"][0:8], 16))
        try:
            self.due = datetime.strftime(datetime.fromisoformat(
                i["due"].replace('Z', '+00:00')), "%Y-%m-%d")
        except:
            self.due = ""
        self.listName = [l.name for l in Lists if l.id == i["idList"]][0]
        self.orderBy = [l.orderBy for l in Lists if l.id == i["idList"]][0]

    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
            'listId': self.listId,
            'desc': self.desc,
            'creationTime': self.creationTime,
            'due': self.due,
            'list': self.listName,
            'orderBy': self.orderBy
        }

    def __str__(self):
        return "Card(id="+self.id+", name="+self.name+")"


class List:
    """
    list class for processing contents of the API
    Return:
        List class object
    """

    def __init__(self, l, i):
        self.id = l["id"]
        self.name = l["name"]
        self.orderBy = i

    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
            'orderBy': self.orderBy
        }

    def __str__(self):
        return "List(id="+self.id+", name="+self.name+", orderBy:"+self.orderBy+")"


class ViewModel:
    def __init__(self, cards, lists):
        self._cards = cards
        self._lists = lists

    @property
    def cards(self):
        return self._cards

    @property
    def lists(self):
        return self._lists
