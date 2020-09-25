import requests
import os

TRELLO_KEY = os.environ.get('TRELLO_KEY')
TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
TRELLO_TODO_BOARDID = os.environ.get('TRELLO_TODO_BOARDID')
TRELLO_TODO_LISTID = os.environ.get('TRELLO_TODO_LISTID')
TRELLO_DONE_LISTID = os.environ.get('TRELLO_DONE_LISTID')

apiurl = "https://api.trello.com/1/"
boardsurl = apiurl + 'boards/'
getcardsonboardsurl = boardsurl + TRELLO_TODO_BOARDID + '/cards'
cardsurl = apiurl + 'cards/'

def getcardsonlist_URL(cardid):
    URL = cardsurl + cardid + "/list"
    return URL
def putcardsonlist_URL(cardid):
    URL = cardsurl + cardid
    return URL

def buildquery(querytype, title=''):
    if querytype == 'getitems':
        return {'key' : TRELLO_KEY, 'token' : TRELLO_TOKEN}
    elif querytype == "saveitem":
        return {'key' : TRELLO_KEY, 'token' : TRELLO_TOKEN, "idList": TRELLO_DONE_LISTID}
    elif querytype == "additem":
        return {'key' : TRELLO_KEY, 'token' : TRELLO_TOKEN, "idList": "5f6076e68cc021208da06d2b", "name" : title}

class Item:
    def __init__(self, id, title, status='To Do'):
        self.id = id
        self.status = status
        self.title = title


def get_items_trello():
    """
    Fetches all cards from the Trello.

    Returns:
        list: The list of saved items.
    """
    cards = requests.get(getcardsonboardsurl, params=buildquery('getitems'))
    cards_json = cards.json()

    items = []
    for card in cards_json:
        cardlist = requests.get(getcardsonlist_URL(card['id']), params=buildquery('getitems'))
        cardlist_json = cardlist.json()
        if cardlist_json['name'] == 'Done':
            cardstatus = 'Completed'
        else :
            cardstatus = cardlist_json['name'] 
        items.append(Item(card['id'], card['name'], cardstatus))
    return items


def save_item_trello(id):
    """
    Updates an existing card in Trello. 

    Args:
        item: The ID of the item to save.
    """
    requests.put(putcardsonlist_URL(id), params=buildquery('saveitem'))
    return id

def add_item_trello(title):
    """
    Adds a new item with the specified title to the Trello To Do list.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    requests.post(cardsurl, params=buildquery('additem', title))
    return 