import requests
from Keys import TrelloApiKey, TrelloServerToken

TODOLISTURL = 'https://api.trello.com/1/lists/5f6f787bf9461c809f224d0d/cards/'
DONELISTURL = 'https://api.trello.com/1/lists/5f6f7883333c1880d598e148/cards/'
ADDTODOLISTURL = 'https://api.trello.com/1/cards/'
TODOLISTID = '5f6f787bf9461c809f224d0d'
CARDSURL = 'https://api.trello.com/1/cards/'
DONELISTID = '5f6f7883333c1880d598e148'


class AccessTrelloApi:

    def __init__(self):
        self.TrelloApiKey = TrelloApiKey
        self.TrelloServerToken = TrelloServerToken

    """
    def getKeys(self):
        f = open('keys.txt', 'r')
        self.TrelloApiKey = f.readline()
        self.TrelloServerToken = f.readline()
        self.TodoListID = f.readline()
        self.DoneListID = f.readline()
    """
    """
    def getCardsFromTodoList(self):
        #ApiValue = 'https://api.trello.com/1/lists/5f6f787bf9461c809f224d0d/cards/?key=64376ab560e7afb4497d897d8cb432b9&token=505e35f027646cbac5cd40afd3617c6cd7e6631b8207636f9eaae8e2c0350069'
        ApiValue2 = TODOLISTURL
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken}
        jsondata = requests.get(ApiValue2, params=payload).json()
        # jsondata = requests.get(ApiValue).json()
        ToDoReturnList = []
        ToDoListDataDict = {}
        for item in jsondata:
            ToDoListDataDict['id'] = item['id']
            ToDoListDataDict['name'] = item['name']
            ToDoListDataDict['status'] = 'To Do'
            CopyOfToDoListDataDict = ToDoListDataDict.copy()
            ToDoReturnList.append(CopyOfToDoListDataDict)
        return ToDoReturnList
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

    def AddItemTodoList(self, name_of_item):
        ApiValue = ADDTODOLISTURL
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken, 'idList': TODOLISTID, 'name': name_of_item}
        requests.post(ApiValue, params=payload)

    def MarkItemAsDone(self, ItemID):
        ApiValue = CARDSURL + ItemID
        payload = {'key': TrelloApiKey,
                   'token': TrelloServerToken, 'idList': DONELISTID}
        requests.put(ApiValue, params=payload)


"""
Test Code
print(obj1.TrelloApiKey)
print(obj1.TrelloServerToken)
print(obj1.TodoListKey)
print(obj1.DoneListKey)
"""
