import requests
from config import api_key, api_token


key = api_key
token = api_token


# api-endpoint
URL = "https://api.trello.com/1/members/me/boards?fields=name,url&key=api_key&token=api_token"


# defining a params dict for the parameters to be sent to the API
PARAMS = {'key': api_key, 'token': api_token}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
board = r.json()


# extracting latitude, longitude and formatted address
# of the first matching location
list = board[0]['id']['name']['desc']


# printing the output
print(list)



key = api_key
token = api_token

# trello_url = "https://api.trello.com/1"
# board_url    = "members/me/boards?" 

# lists = "https://api.trello.com/1/boards/5f38fc5393a450324a0f868f/lists?key=58750588def43275eb1a4457a8efe87d&token=fea90c8a2c8ebf27103def869abcf71abfa536b4d119f8bf3cfd680463f7226f
# cards = "https://api.trello.com/1/lists/5f38fc74a51a6723b3fe75ea/cards?key=58750588def43275eb1a4457a8efe87d&token=fea90c8a2c8ebf27103def869abcf71abfa536b4d119f8bf3cfd680463f7226f



# def goto_trello(url):
    
#     url = "https://api.trello.com/1/lists/5f38fc74a51a6723b3fe75ea/cards?key=58750588def43275eb1a4457a8efe87d&token=fea90c8a2c8ebf27103def869abcf71abfa536b4d119f8bf3cfd680463f7226f"
#     board_url = "https://api.trello.com/1/members/me/boards?fields=name,url&key=api_key&token=api_token"


# def get_board_id():
#         board="https://api.trello.com/1/members/me/boards?fields=name,url&key=api_key&token=api_token"
#         return board[0]["id"]



# class Card:
#     def __init__(self, id, name, desc):
#         self.id = id
#         self.name = name
#         self.name = desc
#         return card

# def get_cards():
#     todo = get_trello('')
#     doing = get_trello()
#     done = get_trello()
#     return card


# def add_new_card():

#     return card
