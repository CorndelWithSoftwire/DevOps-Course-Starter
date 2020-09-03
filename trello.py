import requests
import os
from list import List

def get_lists():
    lists = requests.get(f"https://api.trello.com/1/board/{os.getenv('BOARD_ID')}/lists", params={
        'fields': 'name',
        'key':     os.getenv('SECRET_KEY'),
        'token':   os.getenv('SECRET_TOKEN')
    }).json()

    return { l['id'] : List(l['id'], l['name']) for l in lists }