import requests, json
from flask import session

key = "f8a479ff06b7be92d7bd9d6644a35e82"
token = "4aa46c18e2349cba537fa7169eb9a7733aa16917a12b69d86f44758d8c3faeb2"
uridomain = "https://api.trello.com/1/"
boardid = "J3hiTYRX"

def callTrelloAPI(method,section,call,id,args):
######################################################################################
### REFACTOR THIS ALL TO THIS FORMAT requests.put(url, params={key: value}, args) ####
### requests.put('https://httpbin.org / put', data ={'key':'value'})              ####
######################################################################################
    if(method=="get" and section=="boards" and call=="lists"):
        callurl = "boards/" + id + "/lists?"
    elif(method=="get" and section=="lists" and call=="cards"):
        callurl = "lists/"+ id +"/cards?"
    elif(method=="post" and section=="lists"and call=="cards"):
        callurl = "lists/"+ id +"/cards?name=" + args
    elif(method=="put" and section=="cards"and call==""):
        callurl = "cards/"+ id +"?idList=" + args

    requestUrl = uridomain + callurl + "&key=" + key + "&token=" + token

    if(method == "get"):
        response = requests.get(requestUrl)
    elif(method == "post"):
        response = requests.post(requestUrl)
    elif(method == "put"):
        response = requests.put(requestUrl)

    jsonResponse = json.loads(response.text)
    return jsonResponse

def getListsOnBoards(boardid):  
    "Fetch lists from Trello board and store in session"
    if session.get('lists') is not None:
        return session.get('lists')
    else:
        session['lists'] = callTrelloAPI("get","boards","lists",boardid,"")
        return session.get('lists')
        

def getListId(listofboards, cardname):
    # Get list ID and set in session to save duplicate Trello calls
    if session.get(cardname) is not None:
        return session.get(cardname)
    else:
        for i in listofboards:
                if i['name'] == cardname:
                    break
        session[cardname] = i['id']
        return i['id']

def getCardsOnList(listId):
    # Get cards on a List and add to a new items list to display in HTML
    listofcards = callTrelloAPI("get","lists","cards",listId,"")
    items = []

    for i in listofcards:
        # Create item array
        item = { 'id': i['id'], 'title': i['name'], 'status': 'Things To Do' }
        # Add the item to the list
        items.append(item)
        session['items'] = items

    return items

def get_items():
    #Get cards from "Things To Do" list on Trello
    lists = getListsOnBoards(boardid)    
    getListId(lists,"Things To Do")
    items = getCardsOnList(session.get('Things To Do'))
    return session.get('items', items)


def get_item(id):
    # Get specific card based on its ID
    items = get_items()
    return next((item for item in items if item['id'] == id), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    callTrelloAPI("post", "lists", "cards", session.get('Things To Do'), title)
    items = get_items()
    return items


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

def clearsessions():
    [session.pop(key) for key in list(session.keys())]

def markAsDone(cardId):
    # Move items marks as Done to "Done" list on Trello
    lists = getListsOnBoards(boardid)  
    getListId(lists,"Done")
    callTrelloAPI("put","cards","",cardId, session.get('Done'))