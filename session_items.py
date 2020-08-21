from flask import session

_DEFAULT_ITEMS = []

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    return session.get('items', _DEFAULT_ITEMS)


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

def delete_todo(todo_id):

    print("Todo ID========")
    print(todo_id)
    print("Todo ID========END")


    existing_items = get_items()

    print("Existing Items========")
    print(existing_items)
    print("Existing Items========END")

    session['items'] = [ items for items in existing_items if int(items.get('id')) != int(todo_id) ]

    print("Session Items========")
    print(session['items'])
    print("Session Items========END")


    return todo_id


def complete_todo(id):
  
    existing_items = get_items()

    for item in existing_items:
        if item['id'] == int(id):
            item['status'] = "Completed"
            break

    session['items'] = existing_items

    return id


def started_todo(id):
  
    existing_items = get_items()

    for item in range(len(existing_items)):
        if existing_items[item]['id'] == int(id):
            existing_items[item]['status'] = "Started"
            break

    session['items'] = existing_items

    return id


#update and status buttons

#including the status function 
def update_status(items, status):
    # Check if the passed status is a valid value
    if (status.lower().strip() == 'not started'):
        status = NOTSTARTED
        print("Invalid Status: " + status)
        return None

def update_item(item_id, new_todo_value, new_status_value):
    todo_items = []
    for todo in get_items():
        if int(todo.get('id')) == int(item_id):
            todo['title'] = new_todo_value
            todo['status'] = new_status_value
        todo_items.append(todo)
    session['items'] = todo_items
    return item_id