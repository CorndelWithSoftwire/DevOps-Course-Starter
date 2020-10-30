
import os

from dotenv import load_dotenv

TRELLO_URL = "https://api.trello.com/1/boards/{id}/cards"
LIST_ID_COUNTER = 0
CARD_ID_COUNTER = 0

def get_trello_url():
    return TRELLO_URL

def get_trello_api_key():
    return os.getenv("API_KEY")

def get_trello_board_id():
    return os.getenv("BOARD_ID")

def get_trello_list_id():
    return os.getenv("LIST_ID")

def get_trello_list_id_doing():
    return os.getenv("LIST_ID_DOING")

def get_trello_list_id_done():
    return os.getenv("LIST_ID_DONE")

def get_trello_token():
    return os.getenv("TOKEN")

def get_trello_query():
    query = {'key': get_trello_api_key(),
    'token': get_trello_token()
    }
    return query
    
    