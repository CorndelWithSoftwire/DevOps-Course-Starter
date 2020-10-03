import requests
from Keys import TrelloApiKey, TrelloServerToken

CARDSURL = 'https://api.trello.com/1/cards/'
LISTURL = 'https://api.trello.com/1/lists/'


class Item:

    def __init__(self):
        self.name = ''
        self.id = ''
        self.status = ''

    def GetItemAttributes(self):
        itemAttributes = {'name': self.name,
                          'id': self.id, 'status': self.status}
        return itemAttributes

    def CreateItemInTrello(self, ListID, CardName):
        apiValue = CARDSURL
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken, 'idList': ListID, 'name': CardName}
        jsondata = requests.post(apiValue, params=payload).json()
        self.name = jsondata['name']
        self.id = jsondata['id']
        self.status = jsondata['idList']

    def LoadItemFromTrello(self, CardID):
        apiValue = CARDSURL + CardID + '/'
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken}
        jsondata = requests.get(apiValue, params=payload).json()
        self.name = jsondata['name']
        self.id = jsondata['id']
        self.status = jsondata['idList']

    def GetItemStatusName(self, StatusID):
        apiValue = LISTURL + StatusID
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken}
        jsondata = requests.get(apiValue, params=payload).json()
        return jsondata['name']

    def ChangeItemList(self, NewListID):
        apiValue = CARDSURL + self.id
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken, 'idList': NewListID}
        jsondata = requests.put(apiValue, params=payload).json()
        self.status = jsondata['idList']

    def UpdateName(self, ItemID, NewName):
        apiValue = CARDSURL + ItemID
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken, 'name': NewName}
        jsondata = requests.put(apiValue, params=payload).json()
        self.name = jsondata['name']


obj1 = Item()

obj1.LoadItemFromTrello('5f6f789c6f82ec4d83ca33f5')
# print(obj1.GetItemStatusName(obj1.status))
# obj1.ChangeItemList('5f6f7883333c1880d598e148')
obj1.UpdateName(obj1.id, 'Ironing79')

print(obj1.GetItemAttributes())

atts = obj1.GetItemAttributes()

print(atts['name'])
print(atts['id'])
print(atts['status'])
