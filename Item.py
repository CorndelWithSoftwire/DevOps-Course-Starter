import requests
from Keys import TrelloApiKey, TrelloServerToken
import ApiAccess as api


class Item:

    def __init__(self):
        self.name = ''
        self.id = ''
        self.status = ''

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status

    def get_id(self):
        return self.id

    def GetItemAttributes(self):
        itemAttributes = {'name': self.name,
                          'id': self.id, 'status': self.status}
        return itemAttributes

    def CreateItemInTrello(self, ListID, CardName):
        apiValue = api.CARDSURL
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken, 'idList': ListID, 'name': CardName}
        jsondata = requests.post(apiValue, params=payload).json()
        self.name = jsondata['name']
        self.id = jsondata['id']
        self.status = jsondata['idList']

    def LoadItemFromTrello(self, CardID):
        apiValue = api.CARDSURL + CardID + '/'
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken}
        jsondata = requests.get(apiValue, params=payload).json()
        self.name = jsondata['name']
        self.id = jsondata['id']
        self.status = jsondata['idList']

    def GetItemStatusName(self, StatusID):
        apiValue = api.LISTURL + StatusID
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken}
        jsondata = requests.get(apiValue, params=payload).json()
        return jsondata['name']

    def ChangeItemList(self, NewListID):
        apiValue = api.CARDSURL + self.id
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken, 'idList': NewListID}
        jsondata = requests.put(apiValue, params=payload).json()
        self.status = jsondata['idList']

    def UpdateName(self, ItemID, NewName):
        apiValue = api.CARDSURL + ItemID
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken, 'name': NewName}
        jsondata = requests.put(apiValue, params=payload).json()
        self.name = jsondata['name']
