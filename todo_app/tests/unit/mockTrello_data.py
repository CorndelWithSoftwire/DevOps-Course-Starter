from flask import request
import  os, requests
import pytest

from pytest import MonkeyPatch
from todo_app.tests.unit.mockTrello_reponses import MockResponsesforCard, MockResponsesforList

class mockTrellodata(object):
    Trello_url = "https://api.trello.com/1"
#Trello_url = "https://trello.com/b/i9irJ2QD/trelloboarddevops"


def get_auth():
    return {'key': os.getenv('TRELLO_API_KEY'),
            'token': os.getenv('TRELLO_TOKEN'),
            'boardid' : os.getenv('TRELLO_BOARD_ID')}

def Get_Url_Dict():
    trello_auth = get_auth()
    trello_key = trello_auth['key']
    trello_token = trello_auth['token']
    trello_boardid = trello_auth['boardid']
    trello_keytoken = f"key={trello_key}&token{trello_token}"
    urlDict = {f"https://api.trello.com/1/boards/{trello_boardid}/lists?{trello_keytoken}" }
    return urlDict
  

def mock_get(crudselection, url):
    if(crudselection == 'GET'):
        response = Get_Url_Dict()[url]
    return response

  


