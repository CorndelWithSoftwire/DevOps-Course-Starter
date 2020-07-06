
import os

from dotenv import load_dotenv

TRELLO_URL = "https://api.trello.com/1/boards/{id}/cards"
LIST_ID_COUNTER = 0
CARD_ID_COUNTER = 0

def get_trello_url():
    return TRELLO_URL

def get_trello_api_key():
    load_dotenv()
    return os.getenv("API_KEY")

def get_trello_token():
    load_dotenv()
    return os.getenv("TOKEN")

def get_trello_query():
    query = {'key': get_trello_api_key(),
    'token': get_trello_token()
    }
    return query
    
    