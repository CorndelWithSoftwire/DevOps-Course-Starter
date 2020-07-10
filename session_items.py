import requests, json, os
from flask import session

#key = "f8a479ff06b7be92d7bd9d6644a35e82"
#token = "4aa46c18e2349cba537fa7169eb9a7733aa16917a12b69d86f44758d8c3faeb2"
key = os.environ.get("key", "")
token = os.environ.get("token", "")
uridomain = "https://api.trello.com/1/"
boardid = "J3hiTYRX"

def get_items():
    #Get cards from "Things To Do" list on Trello
    getListsOnBoards(boardid) # get the lists on a board

    # store all ToDo card information from all available lists 
    session['items'] = []
    items = getCardsOnList(session.get('Things To Do'),"Things To Do")
    items = getCardsOnList(session.get('Doing'),"Doing")
    items = getCardsOnList(session.get('Done'),"Done")
    return session.get('items', items)

def getListsOnBoards(boardid):  
    # Fetch lists from Trello board and store in session
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

def getCardsOnList(listId,list):

    if listId is None:
        listId = getListId(session.get('lists'),list) # get list ID for the List
    
        # Get ToDo cards on a List and add to a new items list to display in HTML
    listofcards = callTrelloAPI("get","lists","cards",listId,"")
    if session.get('items') is not None:
        items = session.get('items')
    else:
        items = []

    for i in listofcards:
        # Create item array
        item = { 'id': i['id'], 'title': i['name'], 'status': list }
        #item = new items(i['id'], i['name'], list)
        # Add the item to the list
        items.append(item)
        session['items'] = items

    return items


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

def remove_item(cardId):
    #Delete card on Trello
    callTrelloAPI("delete","cards","",cardId, "")

    #Remove card from Session
    key = cardId
    index = next(index for index, dictionary in enumerate(session.get('items'))
                if dictionary['id'] == key)
    session.get('items').pop(index)

    return session.get('items')

def clearsessions():
    [session.pop(key) for key in list(session.keys())]

def markAsDone(cardId):
    # Move items marks as Done to "Done" list on Trello
    lists = getListsOnBoards(boardid)  
    getListId(lists,"Done")
    callTrelloAPI("put","cards","",cardId, session.get('Done'))

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
    elif(method=="delete" and section=="cards"and call==""):
        callurl = "cards/"+ id +"?" + args

    requestUrl = uridomain + callurl + "&key=" + key + "&token=" + token

    if(method == "get"):
        response = requests.get(requestUrl)
    elif(method == "post"):
        response = requests.post(requestUrl)
    elif(method == "put"):
        response = requests.put(requestUrl)
    elif(method == "delete"):
        response = requests.delete(requestUrl)
    
    try:
        jsonResponse = json.loads(response.text)
    except:
        jsonResponse = ""
        print("No JSON Data returned from Trello")

    return jsonResponse