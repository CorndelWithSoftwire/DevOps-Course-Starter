import requests, json, os
from item import Item

key = os.environ.get("trello_key", "")
token = os.environ.get("trello_token", "")
boardid = os.environ.get("trello_boardid", "")
done_list_id = os.environ.get("done_list_id", "")
doing_list_id = os.environ.get("doing_list_id", "")
todo_list_id = os.environ.get("todo_list_id", "")
uridomain = "https://api.trello.com/1/"


def get_items():
    #Get cards from "Things To Do" list on Trello
    getListsOnBoards(boardid) # get the lists on a board
    items = []
    items.extend(getCardsOnList(todo_list_id,"Things To Do"))
    items.extend(getCardsOnList(done_list_id, "Done"))
    items.extend(getCardsOnList(doing_list_id, "Doing"))
    #items = getCardsOnList(done_list_id)
    #items = getCardsOnList(doing_list_id)
    
    return items 

def getListsOnBoards(boardid):  
    # Fetch lists from Trello board and store in session, if in session then retrive from session

    lists = callTrelloAPI("get","boards","lists",boardid,"")
    return lists
    
        
def getListId(listofcards, cardname):
    # Get list ID and set in session to save duplicate Trello calls

    for i in listofcards:
            if i['name'] == cardname:
                break
    return i['id']

def getCardsOnList(listid, status):

    cards = callTrelloAPI("get","lists","cards",listid,"")

    items = []
    
    for i in cards:
        item_from_list = Item(i['id'],i['name'],i['dateLastActivity'],status).get_items()
        items.append(item_from_list)

    return items


def get_item(id):
    # Get specific card based on its ID
    items = get_items()
    return next((item for item in items if item['id'] == id), None)

def add_item(title):
    # Post item to Trello and retrieve items list from Trello
    callTrelloAPI("post", "lists", "cards", session.get('Things To Do'), title)
    items = get_items()
    return items


def remove_item(cardId):
    #Delete card on Trello
    callTrelloAPI("delete","cards","",cardId, "")

    return 


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
    elif(method=="post" and section=="boards"and call==""):
        callurl = "boards/?name=" + args
    elif(method=="delete" and section=="boards"and call==""):
        callurl = "boards/"+ id +"?" + args

    requestUrl = uridomain + callurl + "&key=" + key + "&token=" + token

    try:
        if(method == "get"):
            response = requests.get(requestUrl)
        elif(method == "post"):
            response = requests.post(requestUrl)
        elif(method == "put"):
            response = requests.put(requestUrl)
        elif(method == "delete"):
            response = requests.delete(requestUrl)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    try:
        jsonResponse = json.loads(response.text)
    except:
        jsonResponse = ""
        print("No JSON Data returned from Trello")

    return jsonResponse

def create_trello_board():
    response = callTrelloAPI("post","boards","","", "TestBoard")

    return response

def delete_trello_board(boardid):
    response = callTrelloAPI("delete","boards","",boardid, "")

    return response
