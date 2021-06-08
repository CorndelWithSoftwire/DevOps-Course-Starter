import requests
import os
import json
from todo_app.data.item import Item

class Trello():
    
    # Initializing the class, accepting Trello key and token as arguments.
    def __init__(self):
        #self.url= "https://api.trello.com/1"
        self.url = "https://api.trello.com/1/boards/"
        self.secret_key = os.getenv('SECRET_KEY')
        self.apikey = os.getenv('TRELLO_API_KEY')
        self.token = os.getenv('TRELLO_TOKEN')
        self.board_id= os.getenv('TRELLO_BOARD_ID')
        self.listid_todo = os.getenv('ID_LIST_TODO')
        self.listid_doing = os.getenv('ID_LIST_DOING')
        self.listid_done = os.getenv('ID_LIST_DONE')
        self.listid_newlist = os.getenv('ID_LIST_NEWLIST')

    def getCardsfromList(self):
        params= {'key': self.apikey, 'token': self.token}
        response =  requests.get(f'https://api.trello.com/1/boards/{self.board_id}/cards', params= params)
        print(response.text)
        items=[]
        for item in response.json():
            if item['idList'] ==self.listid_todo:
                status="ToDo"
            elif item['idList'] == self.listid_done:
                status ='Done'
            item = Item(item['id'], status, item['name'])
            items.append(item)
        return items

    def addCardtodoList(self,cardname):
        params= {'key':self.apikey, 'token':self.token, 'idList':self.listid_todo, 'name':cardname}
        response = requests.post(f'https://api.trello.com/1/cards', params= params)
        print(response.text)

    def moveCardfromtodoListdoing(self, cardid):
        params= {'key':self.apikey, 'token':self.token, 'idList':self.listid_doing}
        response = requests.put(f'https://api.trello.com/1/cards/{cardid}', params= params)
        print(response.text)

    def moveCardfromtodoListdone(self, donecardid):
        params= {'key':self.apikey, 'token':self.token, 'idList':self.listid_done}
        response = requests.put(f'https://api.trello.com/1/cards/{donecardid}', params= params)
        print(response.text)

    def deleteCard(self, cardid):
        params= {'key':self.apikey, 'token':self.token, 'idList':self.listid_doing}
        response = requests.put(f'https://api.trello.com/1/cards/{cardid}', params= params)
        print(response.text)

    def createNewBoard(self, boardname):
        params= {'key':self.apikey, 'token':self.token, 'name':boardname}
        response = requests.post(f'https://api.trello.com/1/boards/', params= params)
        print(response.text)
        boardjson = response.json()
        return boardjson['id']

    def deleteBoard(self, boardid):
        params= {'key':self.apikey, 'token':self.token}
        response = requests.delete(f'https://api.trello.com/1/boards/{boardid}', params= params)
        print(response.text)
        
    


    



