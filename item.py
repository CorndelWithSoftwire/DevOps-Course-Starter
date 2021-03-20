from datetime import datetime
import os

class Item:
    def __init__(self, id, title, datetime, status):
        self.id = id
        self.title = title
        self.status = status
        self.datetime = datetime

    @classmethod
    def from_raw_card(cls, card):
        time = datetime.strptime(card['dateLastActivity'],'%Y-%m-%dT%H:%M:%S.%fZ')
        id = card['_id']
        title = card['name']
        status = card['idList']


        # if trello_card['idList'] == os.environ['todo_list_id']:
        #     status = 'Things To Do'
        # elif trello_card['idList'] == os.environ['doing_list_id']:
        #     status = 'Doing'
        # elif trello_card['idList'] == os.environ['done_list_id']:
        #     status = 'Done'       

        return cls(id, title, time, status)