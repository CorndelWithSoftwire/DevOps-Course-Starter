import requests
import os
from dotenv import load_dotenv
load_dotenv(".env")

api_key =os.getenv('TRELLO_API_KEY')
api_token =os.getenv('TRELLO_API_TOKEN')
idList=os.getenv('ID_LIST')

host = "https://api.trello.com/1"

def make_trello_auth(url):
    """ Attempting to make a trello connection with key and token. """
    trello_url =f"{url}?key={os.getenv('TRELLO_API_KEY')}&token={os.getenv('TRELLO_API_TOKEN')}"
    return(trello_url)

def get_cards_url_with_auth():
    trello_host = "https://api.trello.com/1/cards"
    card_url =f"{trello_host}?key={os.getenv('TRELLO_API_KEY')}&token={os.getenv('TRELLO_API_TOKEN')}"
    return(card_url)


def get_board_id():
    board = make_trello_auth("members/me/boards?")
    return board[0]

# def get_updated_card_url():
#     list_url = "https://api.trello.com/1/cards"
#     formated_url = f"https://api.trello.com/1/lists/{os.getenv('DONE_idList')}cards/?key={os.getenv('TRELLO_API_KEY')}&token={os.getenv('TRELLO_API_TOKEN')}"
#     return(list_url)

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
