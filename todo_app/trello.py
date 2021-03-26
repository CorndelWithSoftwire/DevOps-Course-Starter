import requests
import os
import json

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


class Trello():
    
    # Initializing the class, accepting Trello key and token as arguments.
    def __init__(self):
        self.url= "https://api.trello.com/1"
        #self.url = "https://api.trello.com/1/boards/"

    def getCardsfromList(self):
        params= {'key': api_key, 'token': api_token}
        response =  requests.get(f'https://api.trello.com/1/boards/{board_id}/cards', params= params)
        print(response.text)
        return response


        

