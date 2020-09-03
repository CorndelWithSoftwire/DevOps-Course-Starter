import requests
import os

class Item:
    def __init__(self, name, description, list, id=""):
        self.name = name
        self.description = description
        self.list = list
        self.id = id

    def create(self):
        resp = requests.post(f"https://api.trello.com/1/cards", params={
            'key':     os.getenv('SECRET_KEY'),
            'token':   os.getenv('SECRET_TOKEN'),
            'name': self.name,
            'description': self.description,
            'idList': self.list
        })

        if resp.status_code != 200:
            raise RuntimeWarning(f"Adding card failed: response_code={resp.status_code}")

        resp = resp.json()
        self.id = resp['id']

    def setList(self, newListId):
        resp = requests.put(f"https://api.trello.com/1/cards/{self.id}", params={
            'key':     os.getenv('SECRET_KEY'),
            'token':   os.getenv('SECRET_TOKEN'),
            'idList': newListId
        })

        if resp.status_code != 200:
            raise RuntimeWarning(f"Changing card list failed: response_code={resp.status_code}")

    def delete(self):
        resp = requests.delete(f"https://api.trello.com/1/cards/{self.id}", params={
            'key':     os.getenv('SECRET_KEY'),
            'token':   os.getenv('SECRET_TOKEN'),
        })

        if resp.status_code != 200:
            raise RuntimeWarning(f"Deleting card failed: response_code={resp.status_code}")