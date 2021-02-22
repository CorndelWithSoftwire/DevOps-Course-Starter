import requests, json, os
from item import Item
import sys



def get_items():
    boardid = os.environ["trello_boardid"]
    #Get cards from "Things To Do" list on Trello
    lists = getListsOnBoards(boardid) # get the lists on a board
    setListIdInEnv(lists)

    items = [] 
    cards = callTrelloAPI("get","boards","cards",boardid,"")
    for card in cards:
        item_from_list = Item.from_raw_trello_card(card)
        items.append(item_from_list)

    return items

def getListsOnBoards(boardid):  
    # Fetch lists from Trello board
    lists = callTrelloAPI("get","boards","lists",boardid,"")
    return lists

def get_single_item(id):
    # Get specific card based on its ID
    items = []
    items = get_items()

    return next((items for item in items if item['id'] == id), None)
    
def add_item(title):
    # Post item to Trello and retrieve items list from Trello
    todo_list_id = os.environ["todo_list_id"]
    response = callTrelloAPI("post", "lists", "cards", todo_list_id , title)
    cardid = response["id"]
    return cardid

def remove_item(cardId):
    #Delete card on Trello
    callTrelloAPI("delete","cards","",cardId, "")
    return 

def inprogress_item(cardId):
    #move card to Doing 
    doing_list_id = os.environ["doing_list_id"]
    response = callTrelloAPI("put","cards","",cardId, doing_list_id)
    return doing_list_id == response["idList"]

def markAsDone(cardId):
    # Move items marks as Done to "Done" list on Trello
    done_list_id = os.environ["done_list_id"]
    response = callTrelloAPI("put","cards","",cardId, done_list_id)
    return done_list_id == response["idList"]

def callTrelloAPI(method,section,call,id,args):
######################################################################################
### REFACTOR THIS ALL TO THIS FORMAT requests.put(url, params={key: value}, args) ####
### requests.put('https://httpbin.org / put', data ={'key':'value'})              ####
######################################################################################

    params = (
        ('key', os.environ['trello_key']),
        ('token', os.environ['trello_token']),        
    )

    callurl = ""

    if(method=="get" and section=="boards" and call=="lists"):
        callurl = "boards/" + id + "/lists"
    elif(method=="get" and section=="boards" and call=="cards"):
        callurl = "boards/" + id + "/cards"
    elif(method=="get" and section=="lists" and call=="cards"):
        callurl = "lists/"+ id +"/cards"
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

    requestUrl = "https://api.trello.com/1/" + callurl

    try:
        if(method == "get"):
            response = requests.get(requestUrl, params=params)
        elif(method == "post"):
            response = requests.post(requestUrl, params=params)
        elif(method == "put"):
            response = requests.put(requestUrl, params=params)
        elif(method == "delete"):
            response = requests.delete(requestUrl, params=params)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    try:
        jsonResponse = response.json()
    except:
        jsonResponse = ""
        print("No JSON Data returned from Trello")

    return jsonResponse

def create_trello_board(board_name):
    response = callTrelloAPI("post","boards","","", board_name)
    board_id = response['id']

    return board_id

def delete_trello_board(boardid):
    response = callTrelloAPI("delete","boards","",boardid, "")
    value = response["_value"]

    return value is None

def setListIdInEnv(listofboards):
    # Get list IDs for a Board
    for i in listofboards:
        if i['name'] == "Things To Do":
            os.environ["todo_list_id"] = i['id']
        if i['name'] == "Doing":
            os.environ["doing_list_id"] = i['id']
        if i['name'] == "Done":
            os.environ["done_list_id"] = i['id']

    return 