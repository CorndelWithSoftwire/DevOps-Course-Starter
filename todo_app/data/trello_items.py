import requests

trello_key = ''
trello_token = ''

def get_trello_secrets():
    trello_secrets = []
    with open("todo_app/trello_secrets.txt", 'r') as file:
        split_lines = [line.split('=') for line in file.read().splitlines()]
        trello_secrets = [{'k': k, 'v': v} for [k, v] in split_lines]
    
    for item in trello_secrets:
        k = item['k']
        v = item['v']
        if k == "key":
            trello_key = v
        else:
            trello_token = v

    print( trello_key, trello_token)

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    return session.get('items', _DEFAULT_ITEMS)

get_trello_secrets()