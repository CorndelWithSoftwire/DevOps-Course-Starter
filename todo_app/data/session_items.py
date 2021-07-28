from dotenv.main import find_dotenv, load_dotenv
from flask import session
import requests
import os
import pprint
from datetime import datetime
from dateutil.parser import parse
from todo_app.todo_item import TodoItem

# When running in production, we need to explicitly load the environment variables before they're used in this file
file_path = find_dotenv(".env")
load_dotenv(file_path, override=True)

_DEFAULT_ITEMS = [
    {"id": 1, "status": "Not Started", "title": "List saved todo items"},
    {"id": 2, "status": "Not Started", "title": "Allow new items to be added"},
]
query = {
    "key": os.getenv("Key"),
    "token": os.getenv("Token"),
}

get_cards_url = f"https://api.trello.com/1/boards/{os.getenv('Board_ID')}/cards"


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
    items = get_items()
    for item in items:
        if item["id"] == int(id):
            return item


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()
    url = f"https://api.trello.com/1/cards"
    data = {"idList": os.getenv("to_do_list"), "name": title}
    response = requests.request("POST", url, data=data, params=query)

    
def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = []
    for existing_item in existing_items:
        if item["id"] == existing_item["id"]:
            updated_items.append(item)
        else:
            updated_items.append(existing_item)
    session["items"] = updated_items
    return item


def delete_item(item_id):
    cards = requests.get(get_cards_url, params=query).json()
    for card in cards:
        if card["idShort"] == int(item_id):
            id = card["id"]
            url = f"https://api.trello.com/1/cards/{id}"
            response = requests.delete(url, params=query)


def update_status(string_select_update, item_id):
    cards = requests.get(get_cards_url, params=query).json()
    for card in cards:
        if string_select_update == "In-Progress":
            if card["idShort"] == int(item_id):
                id = card["id"]
                url = f"https://api.trello.com/1/cards/{id}"
                data = {"idList": os.getenv("in_progress_list")}
                response = requests.put(url, data=data, params=query)
        if string_select_update == "To-Do":
            if card["idShort"] == int(item_id):
                id = card["id"]
                url = f"https://api.trello.com/1/cards/{id}"
                data = {"idList": os.getenv("to_do_list")}
                response = requests.put(url, data=data, params=query)
        if string_select_update == "Complete":
            if card["idShort"] == int(item_id):
                id = card["id"]
                url = f"https://api.trello.com/1/cards/{id}"
                data = {"idList": os.getenv("complete_list")}
                response = requests.put(url, data=data, params=query)


def due_date(item_id, due_date_update):
    cards = requests.get(get_cards_url, params=query).json()
    for card in cards:
        if card["idShort"] == int(item_id):
            id = card["id"]
            url = f"https://api.trello.com/1/cards/{id}"
            data = {"due": due_date_update}
            response = requests.put(url, data=data, params=query)
