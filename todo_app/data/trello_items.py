import requests
import json
from flask import session

class Trello_service(object):
    TRELLO_API_URL = 'https://api.trello.com/1/'
    TRELLO_BOARD_ID = '5f6456f8fc414517ed9b0e41'
    TRELLO_CREDENTIALS = ''

    TRELLO_IDLIST = "idList"
    TRELLO_ID_BOARD = 'idBoard'
    TRELLO_ID = "id"
    TRELLO_NAME = "name"

    trello_key = ''
    trello_token = ''
    trello_lists = {}
    items = []

    def __init__(self):
        self.get_trello_secrets()

    def get_trello_secrets(self):
        trello_secrets = []
        with open("todo_app/trello_secrets.txt", 'r') as file:
            split_lines = [line.split('=') for line in file.read().splitlines()]
            trello_secrets = [{'k': k, 'v': v} for [k, v] in split_lines]
        
        for item in trello_secrets:
            k = item['k']
            v = item['v']
            if k == "key":
                self.trello_key = v
            else:
                self.trello_token = v
        
        self.TRELLO_CREDENTIALS = f"key={self.trello_key}&token={self.trello_token}"
        self.get_lists()

    def get_lists(self):
        url = f"{self.TRELLO_API_URL}boards/{self.TRELLO_BOARD_ID}/lists?{self.TRELLO_CREDENTIALS}"
        response = requests.request("GET", url)
        raw_lists = (json.loads(response.text.encode('utf8')))
        for trello_list in raw_lists:
            trelloListDict = dict(name=trello_list[self.TRELLO_NAME], boardId=trello_list[self.TRELLO_ID_BOARD])
            self.trello_lists[trello_list[self.TRELLO_ID]] = trelloListDict

    def get_items(self):
        """
        Fetches all saved items from the session.

        Returns:
            list: The list of saved items.
        """
        url = f"{self.TRELLO_API_URL}boards/{self.TRELLO_BOARD_ID}/cards?{self.TRELLO_CREDENTIALS}"
        response = requests.request("GET", url)
        cards = json.loads(response.text.encode('utf8'))
        i = 0
        for card in cards:
            trelloListDict = self.trello_lists[card[self.TRELLO_IDLIST]]
            itemDict = dict(id=i, cardID=card[self.TRELLO_ID], status=trelloListDict[self.TRELLO_NAME], title=card[self.TRELLO_NAME], listId=card[self.TRELLO_IDLIST] )
            self.items.insert(i, itemDict)
            i += 1
        print(self.items)
        return self.items
       # return session.get('items', self.items)

    def get_item(self, id):
        """
        Fetches the saved item with the specified ID.

        Args:
            id: The ID of the item.

        Returns:
            item: The saved item, or None if no items match the specified ID.
        """
        items = self.get_items()
        return next((item for item in items if item['id'] == int(id)), None)

service = Trello_service()
print(service.get_item(1)) 
