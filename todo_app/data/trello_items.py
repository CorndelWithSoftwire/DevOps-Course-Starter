import requests
import json
from todo_app.data.item import Item
from todo_app.data.trelloList import TrelloList
import todo_app.data.trello_constants as constants

class Trello_service(object):
    trello_lists = {}
    items = []

    def __init__(self):
        self.get_trello_secrets()
        self.get_lists()
        self.get_items_from_trello()

    def get_trello_secrets(self):
        trello_key = ''
        trello_token = ''
        trello_secrets = []
        with open("todo_app/trello_secrets.txt", 'r') as file:
            split_lines = [line.split('=') for line in file.read().splitlines()]
            trello_secrets = [{'k': k, 'v': v} for [k, v] in split_lines]
        
        for item in trello_secrets:
            k = item['k']
            v = item['v']
            if k == "key":
                trello_key = v
            else:
                trello_token = v
        
        constants.TRELLO_CREDENTIALS = f"key={trello_key}&token={trello_token}"

    def get_lists(self):
        """
        Fetches all lists from Trello Api.

        """
        url = f"{constants.TRELLO_API_URL}boards/{constants.TRELLO_BOARD_ID}/lists?{constants.TRELLO_CREDENTIALS}"
        response = requests.request("GET", url)
        raw_lists = (json.loads(response.text.encode('utf8')))
        for trello_list in raw_lists:
            trelloListDict = TrelloList(name=trello_list[constants.TRELLO_NAME], 
                                        boardId=trello_list[constants.TRELLO_ID_BOARD])
            self.trello_lists[trello_list[constants.TRELLO_ID]] = trelloListDict

    def get_list_id(self, name):
        """
        Get a trello list id for a give name from the list of all lists.

        Returns:
            listId:  The identifier for a given name
        """
        for listId in self.trello_lists:
            trello_list = self.trello_lists[listId]
            if trello_list.name == name:
                return listId

    def get_items_from_trello(self):
        """
        Fetches all saved items from Trello.

        Returns:
            list: The list of saved items.
        """
        self.items.clear()
        url = f"{constants.TRELLO_API_URL}boards/{constants.TRELLO_BOARD_ID}/cards?{constants.TRELLO_CREDENTIALS}"
        response = requests.request("GET", url)
        cards = json.loads(response.text.encode('utf8'))
        i = 0
        for card in cards:
            trelloListDict = self.trello_lists[card[constants.TRELLO_IDLIST]]
            item = Item(id=i, 
                        cardID=card[constants.TRELLO_ID], 
                        status=trelloListDict.name, 
                        title=card[constants.TRELLO_NAME], 
                        listId=card[constants.TRELLO_IDLIST] )
            self.items.insert(i, item)
            i += 1
        return self.items

    def get_items(self):
        return self.items

    def get_item(self, id):
        """
        Fetches the saved item with the specified ID.

        Args:
            id: The ID of the item.

        Returns:
            item: The saved item, or None if no items match the specified ID.
        """
        items = self.get_items()
        return next((item for item in items if item.id == int(id)), None)

    def add_item(self, title):
        """
        Adds a new item with the specified title to Trello.

        Args:
            title: The title of the item.

        Returns:
            item: The saved item.
        """
        listId = self.get_list_id('Not Started')
        url = f"{constants.TRELLO_API_URL}/cards?{constants.TRELLO_CREDENTIALS}&idList={listId}&name={title}"
        
        requests.request("POST", url)
        self.get_items_from_trello()

    def save_item(self, item):
        """
        Updates an existing item at Trello. If no existing item matches the ID of the specified item, nothing is saved.

        Args:
            item: The item to save.
        """
        url = f"{constants.TRELLO_API_URL}cards/{item.cardID}?{constants.TRELLO_CREDENTIALS}&idList={item.listId}"
        requests.request("PUT", url)
        self.get_items_from_trello()

    def remove_item(self, id):
        """
        Delete an existing card in the lists.

        Args:
            id: The item's id to delete.
        """
        item = self.get_item(id)
        url = f"{constants.TRELLO_API_URL}cards/{item.cardID}?{constants.TRELLO_CREDENTIALS}&idList={item.listId}"
        requests.request("DELETE", url)
        self.get_items_from_trello()
    