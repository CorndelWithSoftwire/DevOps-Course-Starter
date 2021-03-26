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

    def get_account_details(self):
        "Get the details of the user"
        result_flag = False
        params= {'key': api_key, 'token': api_token}
        get_account_details_url = 'https://api.trello.com/1/members/me/'   
        response = requests.get(url=get_account_details_url,params=params)
        if response.status_code == 200:
            self.boards = response.json()['idBoards']
            result_flag = True
          
        return result_flag  

    def get_board_names(self):
        get_board_url = 'https://api.trello.com/1/members/me/boards'
        params= {'key': api_key, 'token': api_token}
        board_list=[] 
            response = requests.get(url=get_board_url,params=params)
            response = response.json()
            for i in range(len(response)):
                board_list.append(response[i]["name"])
                return board_list

    # def add_list(self,board_name,list_names):
    #     "Add a list for a board"
    #     result_flag = True
       
    #     board_id = self.get_board_id_by_name(board_name)
    #     for list_name in list_names:
    #         ['name'] = list_name
    #         ['idBoard'] = board_id
    #         url = self.url+"/lists/"
    #         response = requests.post(url=url,data=self.key&self.token)
    #         if response.status_code == 200:
    #             result_flag &= True

    #     return result_flag
   
    # def getListDetails():
        
    #     params= {'key': api_key, 'token': api_token}
    #     response =  requests.get(f'https://api.trello.com/1/lists/{listid_newlist}', params= params)
    #     #response =  requests.get(f'https://api.trello.com/1/members/me/?', params= params)
    #     print(response.text)
    #     print(response.json())

    # def getdoingListDetails():
    
    #     params= {'key': api_key, 'token': api_token}
    #     response =  requests.get(f'https://api.trello.com/1/lists/{listid_doing}', params= params)
    #     #response =  requests.get(f'https://api.trello.com/1/members/me/?', params= params)
    #     print(response.text)
    #     print(response.json())


    # def getcardDetails():
        
    #     params= {'key': api_key, 'token': api_token}
    #     response =  requests.get(f'https://api.trello.com/1/cards/{cards_cardOne}', params= params)
    #     #response =  requests.get(f'https://api.trello.com/1/members/me/?', params= params)
    #     print(response.text)
    #     print(response.json())

    # def get_card_id (self,board_name,card_name):
    #     "Get the card id using board name and card name"
    #     board_id = self.get_board_id_by_name(board_name)
    #     card_id = self.get_card_id_by_name(board_id,card_name)
    #     return card_id

    # def get_board_list(self,board_id):
    #     "Get the board id for a board name"
    #     board_list_url = self.url + '/boards/' + board_id +'/lists'
    #     board_details = requests.get(url=board_list_url,params=self.auth)
    #     return board_details.json()

    # def movecardDetails():
        
    #     params= {'key': api_key, 'token': api_token}
    #     response =  requests.put(f'https://api.trello.com/1/cards/{cards_cardOne}', params= params, {listid_doing})
    #     #conn.request("PUT", "/1/cards/605a41e5ab231a6fd025c29a?key=2de5a83f280229944d5715d11c00ff59&token=0fdbf0ca6f756c091754bff9f5848a0591cd21212fddb27373ff332a6ed0f19c&idList=6054b0101e6a3d49645dbdca", payload, headers)
    #     print(response.text)
    #     print(response.json())


    # def createcardDetails():
    #     params= {'key': api_key, 'token': api_token}
    #     response =  requests.post(f'https://api.trello.com/1/cards/{cards_cardOne}', params= params, {listid_doing})
    #     #conn.request("POST", "/1/cards?key=2de5a83f280229944d5715d11c00ff59&token=0fdbf0ca6f756c091754bff9f5848a0591cd21212fddb27373ff332a6ed0f19c&name=ToDoCardThree&idList=6054b0101e6a3d49645dbdc9", payload, headers)
    #     print(response.text)
    #     print(response.json())
    
        

test_obj = Trello(key,token)
#service.getList()            