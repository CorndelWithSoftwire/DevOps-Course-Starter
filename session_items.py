from flask import session
import requests

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    todos = requests.get(
        "https://api.trello.com/1/lists/5f38fc74a51a6723b3fe75ea/cards?key=58750588def43275eb1a4457a8efe87d&token=fea90c8a2c8ebf27103def869abcf71abfa536b4d119f8bf3cfd680463f7226f").json()
    for card in todos:
        print(card)
    return todos
    # return session.get('items', _DEFAULT_ITEMS)

   
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

def delete_item(item):

    # existing_items = get_items()
    # existing_items.remove(item)
    # updated_items = existing_items
    # session['items'] = updated_items
    return item
