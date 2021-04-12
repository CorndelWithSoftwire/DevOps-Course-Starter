import requests
import os
import json
import http.client
from todo_app.flask_config import Config
secret_key = os.getenv('SECRET_KEY')
api_key = os.getenv('TRELLO_API_KEY')
api_token = os.getenv('TRELLO_TOKEN')
board_id= os.getenv('TRELLO_BOARD_ID')
listid_todo = os.getenv('ID_LIST_TODO')
listid_doing = os.getenv('ID_LIST_DOING')
listid_done = os.getenv('ID_LIST_DONE')
listid_newlist = os.getenv('ID_LIST_NEWLIST')
cards_cardOne =os.getenv('CARDS_TODO_CARD_ONE')
cards_cardTwo =os.getenv('CARDS_TODO_CARD_TWO')
cards_cardThree =os.getenv('CARDS_TODO_CARD_THREE')
cards_trelloDone =os.getenv('CARDS_TRELLODONE_CARD')
cards_trelloBoard =os.getenv('CARDS_DEVOPSTRELLOBOARD')


conn = http.client.HTTPSConnection("api.trello.com")
params= {'key': api_key, 'token': api_token}
payload = ''
headers = {
  'Cookie': 'dsc=0bc85f8d929315ed7b49afc5f0177bf17e99c9e36eb73c00a48b936304fd4396'
}

conn.request("GET", "/1/members/me/?{api_key}&{api_token}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
