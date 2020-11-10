import requests
import os, datetime

def get_trello_key():
    trello_key = os.environ.get('TRELLO_KEY')
    return trello_key
    
def get_trello_token():
    trello_token = os.environ.get('TRELLO_TOKEN')
    return trello_token

def get_trello_todo_boardid():
    trello_todo_board_id = os.environ.get('TRELLO_TODO_BOARDID')
    return trello_todo_board_id

def get_trello_todo_listid():
    lists = requests.get(get_lists_on_boards_url(), params=build_auth_query())
    lists_json = lists.json()
    for list in lists_json:
        if list['name'] == "To Do":
            return list['id']

def get_trello_doing_listid():
    lists = requests.get(get_lists_on_boards_url(), params=build_auth_query())
    lists_json = lists.json()
    for list in lists_json:
        if list['name'] == "Doing":
            return list['id']

def get_trello_done_listid():
    lists = requests.get(get_lists_on_boards_url(), params=build_auth_query())
    lists_json = lists.json()
    for list in lists_json:
        if list['name'] == "Done":
            return list['id']


apiurl = "https://api.trello.com/1/"
boardsurl = apiurl + 'boards/'

cardsurl = apiurl + 'cards/'

def getlistofcard_URL(cardid):
    URL = cardsurl + cardid + "/list"
    return URL
def putcardsonlist_URL(cardid):
    URL = cardsurl + cardid
    return URL
def get_cards_on_boards_url():
    getcardsonboardsurl = boardsurl + get_trello_todo_boardid() + '/cards'
    return getcardsonboardsurl
def get_lists_on_boards_url():
    getlistsonboardsurl = boardsurl + get_trello_todo_boardid() + '/lists'
    return getlistsonboardsurl
    
def build_auth_query():
    return {'key' : get_trello_key(), 'token' : get_trello_token()}

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
    cards = requests.get(get_cards_on_boards_url(), params=build_auth_query())
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
        if card['idList'] == get_trello_done_listid():
            cardstatus = 'Done'
        elif card['idList'] == get_trello_doing_listid():
            cardstatus = 'Doing'
        elif card['idList'] == get_trello_todo_listid():
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
    query['idList'] = get_trello_done_listid()
    requests.put(putcardsonlist_URL(id), params=query)
    return id

def mark_item_todo_trello(id):
    """
    sets an existing card in Trello to the todo list

    Args:
        item: The ID of the item to save.
    """
    query = build_auth_query()
    query['idList'] = get_trello_todo_listid()
    requests.put(putcardsonlist_URL(id), params=query)
    return id

def mark_item_doing_trello(id):
    """
    sets an existing card in Trello to the doing list

    Args:
        item: The ID of the item to save.
    """
    query = build_auth_query()
    query['idList'] = get_trello_doing_listid()
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
    query['idList'] = get_trello_todo_listid()
    query['name'] = title
    requests.post(cardsurl, params=query)
    return 