from flask import session
import os
import requests
from todo_app.todo_item import TodoItem


_DEFAULT_ITEMS = [
    {"id": 1, "status": "Not Started", "title": "List saved todo items"},
    {"id": 2, "status": "Not Started", "title": "Allow new items to be added"},
]

get_cards_url = f"https://api.trello.com/1/boards/{os.getenv('BOARD_ID')}/cards"

query = {
    "key": os.getenv("TRELLO_KEY"),
    "token": os.getenv("TRELLO_TOKEN"),
}


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """

    cards = requests.get(get_cards_url, params=query).json()
    items = []
    for card in cards:
        items.append(TodoItem(card))

    return items


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    for item in items:
        if item.id == int(id):
            return item


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """

    url = f"https://api.trello.com/1/cards"
    data = {"idList": os.getenv("LIST_ID_NOT_STARTED"), "name": title}
    response = requests.post(url, data=data, params=query)


def delete_item(item):
    cards = requests.get(get_cards_url, params=query).json()
    for card in cards:
        if card["idShort"] == item.id:
            id = card["id"]
            url = f"https://api.trello.com/1/cards/{id}"
            response = requests.delete(url, params=query)


def mark_in_progress(item):
    cards = requests.get(get_cards_url, params=query).json()
    for card in cards:
        if card["idShort"] == item.id:
            card_id = card["id"]
            url = f"https://api.trello.com/1/cards/{card_id}"
            data = {"idList": os.getenv("LIST_ID_IN_PROGRESS")}
            response = requests.put(url, data=data, params=query)


def mark_complete(item):
    cards = requests.get(get_cards_url, params=query).json()
    for card in cards:
        if card["idShort"] == item.id:
            card_id = card["id"]
            url = f"https://api.trello.com/1/cards/{card_id}"
            data = {"idList": os.getenv("LIST_ID_DONE")}
            response = requests.put(url, data=data, params=query)
