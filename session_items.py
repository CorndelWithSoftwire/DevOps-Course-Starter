import requests, json
from flask import session

""" _DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
] """

key = "f8a479ff06b7be92d7bd9d6644a35e82"
token = "4aa46c18e2349cba537fa7169eb9a7733aa16917a12b69d86f44758d8c3faeb2"
uridomain = "https://api.trello.com/1/"
boardid = "J3hiTYRX"

def callTrelloAPI(method,call,id):

    if(method=="boards" and call=="lists"):
        callmethodurl = "boards/" + id + "/lists"
    elif(method=="lists" and call=="cards"):
        callmethodurl = "lists/"+ id +"/cards"

    requestUrl = uridomain + callmethodurl + "?key=" + key + "&token=" + token
    response = requests.get(requestUrl)
    jsonResponse = json.loads(response.text)
    return jsonResponse

def getTrelloBoards(boardid):  
    return callTrelloAPI("boards","lists",boardid)

def getListId(listofboards, cardname):
    _cardName = cardname
    for i in listofboards:
            if i['name'] == _cardName:
                # print(i['id'])
                break
    return i['id']

def getCardsOnList(listId):
    jsonResponse = callTrelloAPI("lists","cards",listId)
    items = []

    for i in jsonResponse:
        print(i['id'] + " " + i['name']) 
        
        item = { 'id': i['id'], 'title': i['name'], 'status': 'Things To Do' }

        # Add the item to the list
        items.append(item)
        session['items'] = items

    return items

def get_items():
    "Fetch cards from Trello board"
    listofboards = getTrelloBoards(boardid)
    listId = getListId(listofboards,"Things To Do")
    items = getCardsOnList(listId)
    #print(listId)
    return session.get('items', items)


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item

def remove_item(id):
    
    items = get_items()
    key = int(id)

    index = next(index for index, dictionary in enumerate(items)
                if dictionary['id'] == key)

    items.pop(index)
    session['items'] =  items

    return items