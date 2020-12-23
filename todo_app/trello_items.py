import requests

from todo_app.flask_config import Config
from todo_app.item import Item


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    confg = Config()
    not_started_response = requests.get(f'https://api.trello.com/1/lists/{confg.LIST_ID}/cards?key={confg.KEY}&token={confg.TOKEN}')
    done_request = requests.get(f'https://api.trello.com/1/lists/{confg.DONE_LIST_ID}/cards?key={confg.KEY}&token={confg.TOKEN}')
    trello_items = []
    for item in not_started_response.json():
        trello_items.append(Item.from_response(item))
    for item in done_request.json():
        trello_items.append(Item.from_response(item))
    return trello_items


def add_item(title, descr):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    url = "https://api.trello.com/1/cards"

    confg = Config()
    query = {
        'key': confg.KEY,
        'token': confg.TOKEN,
        'idList': confg.LIST_ID,
        'name': title,
        'desc': descr,
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )


def move_to_done(itemId):
    url = f'https://api.trello.com/1/cards/{itemId}'

    headers = {
        "Accept": "application/json"
    }

    confg = Config()
    query = {
        'key': confg.KEY,
        'token': confg.TOKEN,
        'idList': confg.DONE_LIST_ID
    }

    response = requests.request(
        "PUT",
        url,
        headers=headers,
        params=query
    )
