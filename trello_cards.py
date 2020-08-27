import requests
import os
from dotenv import load_dotenv
load_dotenv(".env")

api_key =os.getenv('TRELLO_API_KEY')
api_token =os.getenv('TRELLO_API_TOKEN')
# print(api_key)
# print(api_token)
host = "https://api.trello.com/1"
url = "fields=name,url,desc,idBoardSource,dateLastViewid"

def make_trello_auth(url):
    """ Attempting to make a trello connection with key and token. """
    trello_url =f"{url}?key={os.getenv('TRELLO_API_KEY')}&token={os.getenv('TRELLO_API_TOKEN')}"
    return(trello_url)

def get_trello_url(url):
    other_trello_url = make_trello_auth(url)
    response = "requests.get(url=other_trello_url).json()"
    print(other_trello_url)
    return response

def get_board_id():
    board = make_trello_auth("members/me/boards?")
    return board[0]




# def goto_trello(url):
    
#     url = "https://api.trello.com/1/lists/5f38fc74a51a6723b3fe75ea/cards?key=58750588def43275eb1a4457a8efe87d&token=fea90c8a2c8ebf27103def869abcf71abfa536b4d119f8bf3cfd680463f7226f"
#     board_url = "https://api.trello.com/1/members/me/boards?fields=name,url&key=api_key&token=api_token"


# def get_board_id():
#     board="https://api.trello.com/1/members/me/boards?fields=name,url&key=api_key&token=api_token"
# return board[0]["id"]

# def get_list_id():

    # return

# class Card:


#     def __init__(self, id, name, desc):
#         self.id = id
#         self.name = name
#         self.desc = desc
#     return card

#     def get_cards():
#         todo = get_trello_url("members/me/boards?")
#         doing = get_trello()
#         done = get_trello()
#     return todo
