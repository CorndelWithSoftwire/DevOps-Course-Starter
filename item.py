from datetime import datetime
import os

class Item:
    def __init__(self, id, title, datetime, status):
        self.id = id
        self.title = title
        self.status = status
        self.datetime = datetime

    @classmethod
    def from_raw_trello_card(cls, trello_card):
        time = datetime.strptime(trello_card['dateLastActivity'],'%Y-%m-%dT%H:%M:%S.%fZ')
        id = trello_card['id']
        title = trello_card['name']

        if trello_card['idList'] == os.environ['todo_list_id']:
            status = 'Things To Do'
        elif trello_card['idList'] == os.environ['doing_list_id']:
            status = 'Doing'
        elif trello_card['idList'] == os.environ['done_list_id']:
            status = 'Done'       

        return cls(id, title, time, status)