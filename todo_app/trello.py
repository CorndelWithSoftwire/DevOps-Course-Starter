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
# cards_cardOne =os.getenv('CARDS_TODO_CARD_ONE')
# cards_cardTwo =os.getenv('CARDS_TODO_CARD_TWO')
# cards_cardThree =os.getenv('CARDS_TODO_CARD_THREE')
# cards_trelloDone =os.getenv('CARDS_TRELLODONE_CARD')
# cards_trelloBoard =os.getenv('CARDS_DEVOPSTRELLOBOARD')


class Trello():
    
    # Initializing the class, accepting Trello key and token as arguments.
    def __init__(self):
        self.url= "https://api.trello.com/1"
        #self.url = "https://api.trello.com/1/boards/"

    def getCardsfromList(self):
        params= {'key': api_key, 'token': api_token}
        response =  requests.get(f'https://api.trello.com/1/boards/{board_id}/cards', params= params)
        print(response.text)
        items=[]
        for item in response.json():
            if item['idList'] ==listid_todo:
                status="ToDo"
            elif item['idList'] == listid_done:
                status ='Done'
            items.append({'id':item['id'], 'status':status, 'title': item['name']})
        return items

    def addCardtodoList(self,cardname):
        params= {'key':api_key, 'token':api_token, 'idList':listid_todo, 'name':cardname}
        response = requests.post(f'https://api.trello.com/1/cards', params= params)
        print(response.text)

    def moveCardfromtodoListdoing(self, cardid):
        params= {'key':api_key, 'token':api_token, 'idList':listid_doing}
        response = requests.put(f'https://api.trello.com/1/cards/{cardid}', params= params)
        print(response.text)

    def moveCardfromtodoListdone(self, donecardid):
        params= {'key':api_key, 'token':api_token, 'idList':listid_done}
        response = requests.put(f'https://api.trello.com/1/cards/{donecardid}', params= params)
        print(response.text)

    def deleteCard(self, cardid):
        params= {'key':api_key, 'token':api_token, 'idList':listid_doing}
        response = requests.put(f'https://api.trello.com/1/cards/{cardid}', params= params)
        print(response.text)









    # def getboardid(self, boardid):
    #     params= {'key': api_key, 'token': api_token}
    #     response =  requests.get(f'https://api.trello.com/1/boards/{board_id}', params= params)
    #     print(response.text)
     


    



