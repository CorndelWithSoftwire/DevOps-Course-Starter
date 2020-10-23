import requests
import os, datetime

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
    def __init__(self, id, title, lastmodifieddate, status='To Do'):
        self.id = id
        self.status = status
        self.title = title
        self.lastmodifieddate = lastmodifieddate

def get_items_from_trello_api():
    """
    Fetches all cards from the Trello.

    Returns:
        list: Json formatted list from Trello
    """
    cards = requests.get(getcardsonboardsurl, params=build_auth_query())
    cards_json = cards.json()
    return cards_json

def get_items_trello():
    """
    Fetches all cards from the Trello.

    Returns:
        list: The list of saved items.
    """
    cards_json = get_items_from_trello_api()

    items = []
    for card in cards_json:
        if card['idList'] == TRELLO_DONE_LISTID:
            cardstatus = 'Done'
        elif card['idList'] == TRELLO_DOING_LISTID:
            cardstatus = 'Doing'
        elif card['idList'] == TRELLO_TODO_LISTID:
            cardstatus = "To Do"
        else:
            raise AttributeError
        Lastactivity_Trello = card['dateLastActivity']
        LastActivity = datetime.datetime.strptime(Lastactivity_Trello, '%Y-%m-%dT%H:%M:%S.%fZ').date()
        items.append(Item(card['id'], card['name'], LastActivity, cardstatus))
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