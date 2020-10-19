import requests
import os

TRELLO_KEY = os.environ.get('TRELLO_KEY')
TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
TRELLO_TODO_BOARDID = os.environ.get('TRELLO_TODO_BOARDID')
TRELLO_TODO_LISTID = os.environ.get('TRELLO_TODO_LISTID')
TRELLO_DOING_LISTID = os.environ.get('TRELLO_DOING_LISTID')
TRELLO_DONE_LISTID = os.environ.get('TRELLO_DONE_LISTID')

apiurl = "https://api.trello.com/1/"
boardsurl = apiurl + 'boards/'
getcardsonboardsurl = boardsurl + TRELLO_TODO_BOARDID + '/cards'
cardsurl = apiurl + 'cards/'

def getlistofcard_URL(cardid):
    URL = cardsurl + cardid + "/list"
    return URL
def putcardsonlist_URL(cardid):
    URL = cardsurl + cardid
    return URL

def build_auth_query():
    return {'key' : TRELLO_KEY, 'token' : TRELLO_TOKEN}

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
    cards = requests.get(getcardsonboardsurl, params=build_auth_query())
    cards_json = cards.json()

    items = []
    for card in cards_json:
        cardlist = requests.get(getlistofcard_URL(card['id']), params=build_auth_query())
        cardlist_json = cardlist.json()
        if cardlist_json['name'] == 'Done':
            cardstatus = 'Done'
        elif cardlist_json['name'] == 'Doing':
            cardstatus = 'Doing'
        else :
            cardstatus = cardlist_json['name'] 
        items.append(Item(card['id'], card['name'], cardstatus))
    return items


def mark_item_done_trello(id):
    """
    sets an existing card in Trello to the done list

    Args:
        item: The ID of the item to save.
    """
    query = build_auth_query()
    query['idList'] = TRELLO_DONE_LISTID
    requests.put(putcardsonlist_URL(id), params=query)
    return id

def mark_item_todo_trello(id):
    """
    sets an existing card in Trello to the todo list

    Args:
        item: The ID of the item to save.
    """
    query = build_auth_query()
    query['idList'] = TRELLO_TODO_LISTID
    requests.put(putcardsonlist_URL(id), params=query)
    return id

def mark_item_doing_trello(id):
    """
    sets an existing card in Trello to the doing list

    Args:
        item: The ID of the item to save.
    """
    query = build_auth_query()
    query['idList'] = TRELLO_DOING_LISTID
    requests.put(putcardsonlist_URL(id), params=query)
    return id

def add_item_trello(title):
    """
    Adds a new item with the specified title to the Trello To Do list.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    query = build_auth_query()
    query['idList'] = TRELLO_TODO_LISTID
    query['name'] = title
    requests.post(cardsurl, params=query)
    return 