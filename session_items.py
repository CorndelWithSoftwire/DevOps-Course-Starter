from flask import session

import requests
import os

_DEFAULT_ITEMS = []

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    # return session.get('items', _DEFAULT_ITEMS)
    payload = {'key': os.getenv('trello_key'), 'token': os.getenv('trello_token')}
    r = requests.get(f'https://api.trello.com/1/lists/{os.getenv("trello_todo_list")}/cards', params=payload)
    list = []
 
    for item in r.json():
        list_item = {"title":item['name'],"id":item["id"],"status":"todo"}
        list.append(list_item)
 
    return list


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    # items = get_items()

    # # Determine the ID for the item based on that of the previously added item
    # id = items[-1]['id'] + 1 if items else 0

    # item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # # Add the item to the list
    # items.append(item)
    # session['items'] = items

    # return item

    payload = {'key': os.getenv('trello_key'), 'token': os.getenv('trello_token','idList': '5f451c994e05398abae2ebe2', 'name': title})}
    r = requests.post('https://api.trello.com/1/Cards', params=payload)




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
    existing_items = get_items()
    session['items'] = [ items for items in existing_items if int(items.get('id')) != int(todo_id) ]
    return todo_id

     payload = {'key': os.getenv('trello_key'), 'token': os.getenv('trello_token','idList': '5f451c994e05398abae2ebe2', 'name': title})}
    r = requests.post('https://api.trello.com/1/Cards', params=payload)


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

def update_status(items, status):
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