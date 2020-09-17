from secrets import KEY, TOKEN
import requests

todo_boardid = "5f6076c34c5f48265943e31e"
todolistid = "5f6076e68cc021208da06d2b"
donelistid = "5f6076e96994a166c05385a6"

apiurl = "https://api.trello.com/1/"
boardsurl = apiurl + 'boards/'
getcardsonboardsurl = boardsurl + todo_boardid + '/cards'
cardsurl = apiurl + 'cards/'

def getcardsonlist_URL(cardid):
    URL = cardsurl + cardid + "/list"
    return URL
def putcardsonlist_URL(cardid):
    URL = cardsurl + cardid
    return URL

def buildquery(querytype, title=''):
    if querytype == 'getitems':
        return {'key' : KEY, 'token' : TOKEN}
    elif querytype == "saveitem":
        return {'key' : KEY, 'token' : TOKEN, "idList": donelistid}
    elif querytype == "additem":
        return {'key' : KEY, 'token' : TOKEN, "idList": "5f6076e68cc021208da06d2b", "name" : title}

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