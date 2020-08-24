import requests
import secrets
from card import Card

key = secrets.apiKey
token = secrets.apiToken

def get_todo_cards_for_board():
    """
    Fetches all To Do cards from the board.

    Returns:
        list: The list of cards.
    """

    query = {
        'key': key,
        'token': token
    }
   
    board_id = secrets.boardId
    to_do_cards = []
    url = "https://api.trello.com/1/boards/{}/cards".format(board_id)
    cards = requests.request("GET", url, params=query)
    for card in cards.json():
        if (get_list_name(card['id']) == 'To Do'):
            to_do_cards.append(Card(card['id'], card['pos'], card['name'], card['desc'], get_list_name(card['id'])))
    return to_do_cards

def get_cards_for_board():
    """
    Fetches all To Do cards from the board.

    Returns:
        list: The list of cards.
    """

    query = {
        'key': key,
        'token': token
    }
   
    board_id = secrets.boardId
    all_cards = []
    url = "https://api.trello.com/1/boards/{}/cards".format(board_id)
    cards = requests.request("GET", url, params=query)
    for card in cards.json():
        all_cards.append(Card(card['id'], card['pos'], card['name'], card['desc'], get_list_name(card['id'])))
    return all_cards

def get_list_name(card_id):
    """
    Gets the list name a specific card is in, based on the card's id.
    Returns:
        string: The list's name.
    """
    url = "https://api.trello.com/1/cards/{}/list".format(card_id)
    query = {
        'key': key,
        'token': token
    }
    list = requests.request("GET", url, params=query)
    return list.json()['name']


def create_item(title, description):
    """
    Creates a card in the TO DO list of the board.
    Returns:
        Card: The newly created Card object.
    """
    url = "https://api.trello.com/1/cards"
    query = {
        'key': key,
        'token': token,
        'name': title, 
        'desc': description,
        'pos': len(get_cards_for_board()) + 1, 
        'idList': '5f3a9a92b421455eaa2ca175' # this is the id for the 'To Do' list
    }
    card = requests.request("POST", url, params=query)
    return card


def complete_item(item_id):
    """
    Moves a card to the 'DONE' list of the board.
    """
    id_list = "5f3a9a92b421455eaa2ca177" # this is the id for the 'Done' list
    url = "https://api.trello.com/1/cards/{}".format(item_id)
    query = {
        'key': key,
        'token': token,
        'idList': id_list
    }
    requests.request("PUT", url, params=query)


def undo_item(item_id):
    """
    Moves a card to the 'TODO' list of the board.
    """
    id_list = '5f3a9a92b421455eaa2ca175' # this is the id for the 'To Do' list
    url = "https://api.trello.com/1/cards/{}".format(item_id)
    query = {
        'key': key,
        'token': token,
        'idList': id_list
    }
    requests.request("PUT", url, params=query)
