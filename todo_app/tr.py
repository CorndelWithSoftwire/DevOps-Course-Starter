import requests
import os
import json
import http.client

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

url = "https://api.trello.com/1/lists/6054b0101e6a3d49645dbdc9/?"
query = {'key': {api_key}, 'token': {api_token}}
#query = {   'key': '2de5a83f280229944d5715d11c00ff59',   'token': '0fdbf0ca6f756c091754bff9f5848a0591cd21212fddb27373ff332a6ed0f19c'}
response = requests.request("GET", url, params=query)
print(response.text)



conn = http.client.HTTPSConnection("api.trello.com")
payload = ''
headers = {
  'Cookie': 'dsc=0bc85f8d929315ed7b49afc5f0177bf17e99c9e36eb73c00a48b936304fd4396'
}
conn.request("GET", "/1/cards/{cards_cardOne}?key=2de5a83f280229944d5715d11c00ff59&token=0fdbf0ca6f756c091754bff9f5848a0591cd21212fddb27373ff332a6ed0f19c", payload, headers)
#conn.request("GET", "/1/cards/6054b0789b71d43acb0d5581?key=2de5a83f280229944d5715d11c00ff59&token=0fdbf0ca6f756c091754bff9f5848a0591cd21212fddb27373ff332a6ed0f19c", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


#conn.request("GET", "/1/cards/6054b0789b71d43acb0d5581?key=2de5a83f280229944d5715d11c00ff59&token=0fdbf0ca6f756c091754bff9f5848a0591cd21212fddb27373ff332a6ed0f19c", payload, headers)





# def __init__(self, apikey, token=None):
#         self._apikey = apikey
#         self._token = token

# def get(self, listid_todo):
#     url = "https://trello.com/1/lists/{listid_todo}"
#    # query = {'key': api_key, 'token': api_token}
#     query = {   'key': '2de5a83f280229944d5715d11c00ff59',   'token': '0fdbf0ca6f756c091754bff9f5848a0591cd21212fddb27373ff332a6ed0f19c'}
#     response = requests.request("GET", url, params=query)
#     print(response.text)
# # resp = requests.get(f"https://trello.com/1/lists/{listid_todo}", params={"key": self._apikey, "token": self._token, "cards": cards}, data=None)
# # print(response.text)
# #return self.raise_or_json(resp)


# api_key = os.getenv('TRELLO_API_KEY')
# api_token = os.getenv('TRELLO_TOKEN')
# board_id= os.getenv('TRELLO_BOARD_ID')
# listid_todo = os.getenv('ID_LIST_TODO')
# listid_doing = os.getenv('ID_LIST_DOING')
# listid_done = os.getenv('ID_LIST_DONE')
# listid_newlist = os.getenv('ID_LIST_NEWLIST')
# cards_cardOne =os.getenv('CARDS_TODO_CARD_ONE')
# cards_cardTwo =os.getenv('CARDS_TODO_CARD_TWO')
# cards_cardThree =os.getenv('CARDS_TODO_CARD_THREE')
# cards_trelloDone =os.getenv('CARDS_TRELLODONE_CARD')
# cards_trelloBoard =os.getenv('CARDS_DEVOPSTRELLOBOARD')