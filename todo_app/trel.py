import requests
import conf as conf
from datetime import datetime

class Trello_Util:
    " Trello util to create board, card, copy card and add members"    

    def __init__(self,key,token):
        self.auth = {'key':key,'token':token}
        self.url= "https://api.trello.com/1"
        self.headers = {
            'type': "type",
            'content-type': "application/json"
                }


    def get_account_details(self):
        "Get the details of the user"
        result_flag = False
        get_account_details_url = 'https://api.trello.com/1/members/me/'
        try:
            response = requests.get(url=get_account_details_url,params=self.auth)
            if response.status_code == 200:
                self.boards = response.json()['idBoards']
                result_flag = True
        except Exception as e:
            print str(e)
    
        return result_flag

    
    def get_board_names(self):
        get_board_url = 'https://api.trello.com/1/members/me/boards'
        board_list=[]
        try:
            response = requests.get(url=get_board_url,params=self.auth)
            response = response.json()
            for i in range(len(response)):
                board_list.append(response[i]["name"])
        except Exception as e:
            print str(e)
        return board_list

    
    def add_board(self,board_name):
        "Add board using board name"
        result_flag = False
        self.payload = self.auth.copy()
        self.payload['name'] = board_name
        self.payload['defaultLists'] = "false"
        url = self.url+"/boards/"
        response = requests.post(url=url,data=self.payload)
        if response.status_code == 200:
            result_flag = True

        return result_flag


    def add_member_board(self,new_board_name,email_ids):
        " Add members to the board"
        result_flag = True
        board_id = self.get_board_id_by_name(new_board_name)
        url = self.url+"/boards/"+board_id +"/members"
        headers = self.headers
        for email_id in email_ids:
            self.payload = self.auth.copy()
            self.payload['email']= email_id
            response = requests.request("PUT", url, headers=headers, params=self.payload)
            if response.status_code == 200:
                result_flag &= True
            else:
                result_flag &= False

        return result_flag


    def add_member_card(self,new_board_name,card_name,member_username):
        " Add members to the board"
        result_flag = True
        member_list_id = []
        board_id = self.get_board_id_by_name(new_board_name)
        card_id = self.get_card_id_by_name(board_id,card_name)
        member_url = self.url+"/boards/"+board_id +"/members"
        response = requests.get(url=member_url,params=self.auth)
        response = response.json()
        for i in range(len(response)):
            if response[i]['username'] in member_username:
                member_list_id.append(response[i]['id'])
        for member_id  in member_list_id:
            member_post_url= self.url+'/cards/'+card_id+'/idMembers'
            self.payload = self.auth.copy()
            self.payload['value'] = member_id
            response = requests.post(url=member_post_url,params=self.payload)
            if response.status_code == 200:
                result_flag &= True
            else :
                result_flag &=False        

        return result_flag

    def add_list(self,board_name,list_names):
        "Add a list for a board"
        result_flag = True
        self.payload = self.auth.copy()
        board_id = self.get_board_id_by_name(board_name)
        for list_name in list_names:
            self.payload['name'] = list_name
            self.payload['idBoard'] = board_id
            url = self.url+"/lists/"
            response = requests.post(url=url,data=self.payload)
            if response.status_code == 200:
                result_flag &= True

        return result_flag


    def copy_card(self,org_board_name,org_card_names,new_board_name,new_list_name):
        "Copy card to board"
        result_flag = True
        self.card_payload = self.auth.copy()
        list_id  = self.get_list_id(new_board_name,new_list_name)
        self.card_payload['idList'] = list_id
        card_url = self.url+'/cards'
        for org_card_name in org_card_names:
            card_id = self.get_card_id(org_board_name,org_card_name)
            self.card_payload['idCardSource'] = card_id
            response = requests.post(url=card_url,params=self.card_payload)
            if response.status_code == 200:
                result_flag &= True
            else :
                result_flag &= False

        return result_flag
        '''
        var payload = {"due": "",
               "idList":copyList,
               "idCardSource":cardID,
               "keepFromSource":attachments
              };
        '''

    
    def get_card_id (self,board_name,card_name):
        "Get the card id using board name and card name"
        board_id = self.get_board_id_by_name(board_name)
        card_id = self.get_card_id_by_name(board_id,card_name)
        return card_id

    
    def get_list_id(self,board_name,list_name):
        "Get the list id where you are adding the new cards"
        board_id = self.get_board_id_by_name(board_name)
        board_list = self.get_board_list(board_id)
        for i in range(len(board_list)):
            if board_list[i]['name'] == list_name:
                board_list_id = board_list[i]['id']
        return board_list_id


    def get_card_id_by_name(self,board_id,card_name):
        "Get the card id"
        card_id = None
        card_url = self.url + '/boards/' + board_id +'/cards'
        card_details = requests.get(url=card_url,params=self.auth)
        card_details = card_details.json()
        for i in range(len(card_details)):
            if card_details[i]['name'] == card_name:
                card_id = card_details[i]['id']
        return card_id            
           
    
    def get_board_id_by_name(self,board_name):
        "Get the board id for a board name"
        board_id = None
        self.get_account_details()
        for board in self.boards:    
            board_url = self.url + '/boards/' + board
            board_details = requests.get(url=board_url,params=self.auth)
            board_details = board_details.json()
            if board_details['name']  == board_name:
                board_id = board
        return board_id


    def get_board_list(self,board_id):
        "Get the board id for a board name"
        board_list_url = self.url + '/boards/' + board_id +'/lists'
        board_details = requests.get(url=board_list_url,params=self.auth)
        return board_details.json()

    
    def change_preferences(self,board_name,pref):
        # change the visibility/preferences of a board
        result_flag = True
        board_id = self.get_board_id_by_name(board_name)
        url = self.url+"/boards/"+board_id
        self.payload = self.auth.copy()
        self.payload['prefs/permissionLevel'] = pref    
        response = requests.put(url=url,params=self.payload)
        if response.status_code == 200:
                result_flag &= True
        else:
            result_flag &= False
        return result_flag


    def get_last_board(self):
        "Get all the boards"        
        for board in self.boards:
            #response = response.json()
            board_url = self.url + '/boards/' + board
            response = requests.get(url=board_url,params=self.auth)
            response = response.json()
            id_board = board
            print (datetime.fromtimestamp(int(id_board[0:8],16)))