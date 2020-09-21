import requests
import json
class Trello_service(object):
    TRELLO_API_URL = 'https://api.trello.com/1/'
    TRELLO_BOARD_ID = '5f6456f8fc414517ed9b0e41'
    TRELLO_CREDENTIALS = ''

    trello_key = ''
    trello_token = ''
    trello_lists = {}
    items = []

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
            trelloListDict = dict(name=trello_list['name'], boardId=trello_list['idBoard'])
            self.trello_lists[trello_list['id']] = trelloListDict

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
            trelloListDict = self.trello_lists[card['idList']]
            itemDict = dict(id=card['id'], status=trelloListDict['name'], title=card['name'], listId=card['idList'] )
            self.items.insert(i, itemDict)
            i += 1
        print(self.items)
        #return session.get('items', _DEFAULT_ITEMS)

service = Trello_service()
service.get_trello_secrets()
service.get_items() 
