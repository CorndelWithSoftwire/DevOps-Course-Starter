from flask import session

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items sorted by status and then by ID.
    """
    return sorted(session.get('items', _DEFAULT_ITEMS), key=lambda item : (item['status'], item['id']), reverse=True)


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

    # Determine the next ID for the item based on max ID in the session or if not available on the last item or if empty set to 1
    # this guarantees a new true ID is created all the time (avoiding the scenario when deleting the last ID)
    if session.get('maxId'):
        id = session['maxId'] +1 
    elif items:
        id = items[0]['id'] + 1
    else:
        id = 1
        
    session['maxId'] = id

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
    """
    Deletes a specific item from the session.

    Args:
        item: The item to delete.

    """
    existing_items = get_items()
    updated_items = [existing_item for existing_item in existing_items if item['id'] != existing_item['id']]

    session['items'] = updated_items

    return item