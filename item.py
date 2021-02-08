from datetime import datetime

class Item:
    def __init__(self, id, title, datetime, status):
        self.id = id
        self.title = title
        self.status = status
        self.datetime = datetime

    @classmethod
    def from_raw_trello_card(cls, trello_card, status):
        time = datetime.strptime(trello_card['dateLastActivity'],'%Y-%m-%dT%H:%M:%S.%fZ')
        id = trello_card['id']
        title = trello_card['name']

        return cls(id, title, time, status)