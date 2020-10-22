from tests.mock_responses import MockCardsResponse, MockListsResponse
import pytest
import os, requests
from todo_app.data.trello_constants import TRELLO_API_URL

def get_auth_params():
    return { 'key': os.getenv('TRELLO_KEY'), 
            'token': os.getenv('TRELLO_TOKEN'),
            'list': os.getenv('TRELLO_BOARD_ID')}

def mock_trello_handler(monkeypatch):
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response is set to successful
    THEN check the HTTP response
    """
    trello_config = get_auth_params()
    trello_key = trello_config ['key']
    trello_token = trello_config ['token']
    trello_default_board = trello_config ['list']
    trello_credentials = f"key={trello_key}&token={trello_token}"

    urlDict = { f"{TRELLO_API_URL}boards/{trello_default_board}/lists?{trello_credentials}" : MockListsResponse(),
               f"{TRELLO_API_URL}boards/{trello_default_board}/cards?{trello_credentials}" : MockCardsResponse() }

    def mock_get(verb, url):
        response = urlDict.get(url)
        return response
    
    monkeypatch.setattr(requests, 'request', mock_get)