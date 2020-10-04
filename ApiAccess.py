import requests
from Keys import TrelloApiKey, TrelloServerToken

TODOLISTURL = 'https://api.trello.com/1/lists/5f6f787bf9461c809f224d0d/cards/'
DONELISTURL = 'https://api.trello.com/1/lists/5f6f7883333c1880d598e148/cards/'
CARDSURL = 'https://api.trello.com/1/cards/'
LISTURL = 'https://api.trello.com/1/lists/'
TODOLISTID = '5f6f787bf9461c809f224d0d'
DONELISTID = '5f6f7883333c1880d598e148'


class AccessTrelloApi:

    """
        Returns cards from Trello based on the list name.
    """

    def getCardsFromTrelloList(self, ListURL, ListName):
        ApiValue = ListURL
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken}
        jsondata = requests.get(ApiValue, params=payload).json()
        ReturnList = []
        ListDataDict = {}
        for item in jsondata:
            ListDataDict['id'] = item['id']
            ListDataDict['name'] = item['name']
            ListDataDict['status'] = ListName
            CopyOfListDataDict = ListDataDict.copy()
            ReturnList.append(CopyOfListDataDict)
        return ReturnList

    """
        Adds and Item to the todo list
    """

    def AddItemTodoList(self, name_of_item):
        ApiValue = CARDSURL
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken, 'idList': TODOLISTID, 'name': name_of_item}
        requests.post(ApiValue, params=payload)

    """
        Takes item id and adds to the done list
    """

    def MarkItemAsDone(self, ItemID):
        ApiValue = CARDSURL + ItemID
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken, 'idList': DONELISTID}
        requests.put(ApiValue, params=payload)
