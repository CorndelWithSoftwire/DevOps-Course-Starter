from secrets import KEY, TOKEN
import requests

def get_items_trello():
    """
    Fetches all cards from the Trello.

    Returns:
        list: The list of saved items.
    """
    apiurl = "https://api.trello.com/1/"
    boardsurl = "boards/5f6076c34c5f48265943e31e/"
    cardsurl = "cards/"
    query = {'key' : KEY, 'token' : TOKEN}
    cards = requests.get(apiurl+boardsurl+"cards", params=query)
    cards_json = cards.json()

    items = []
    for card in cards_json:
        cardlist = requests.get(apiurl+cardsurl+card['id']+"/list", params=query)
        cardlist_json = cardlist.json()
        if cardlist_json['name'] == 'Done':
            cardstatus = 'Completed'
        else :
            cardstatus = cardlist_json['name'] 
        items.append({"id" : card['id'], "status": cardstatus, "title": card['name']})
    return items


def save_item_trello(id):
    """
    Updates an existing card in Trello. 

    Args:
        item: The ID of the item to save.
    """
    url = "https://api.trello.com/1/cards/" + id
    query = {'key' : KEY, 'token' : TOKEN, "idList": "5f6076e96994a166c05385a6"}
    requests.put(url, params=query)
    return id

def add_item_trello(title):
    """
    Adds a new item with the specified title to the Trello To Do list.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    url = "https://api.trello.com/1/cards/"
    query = {'key' : KEY, 'token' : TOKEN, "idList": "5f6076e68cc021208da06d2b", "name" : title}
    requests.post(url, params=query)
    return 