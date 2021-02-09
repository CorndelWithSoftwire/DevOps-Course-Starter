import os
from datetime import datetime

class Card:
    def __init__(self, id, name, desc, status, modified_date = datetime.now()):
        self.id = id
        self.name = name
        self.desc = desc
        self.status = status
        self.modified_date = modified_date

    @classmethod
    def from_raw_trello_card(cls, trello_card):
        id_list = trello_card["idList"]

        status = ""
        if id_list == os.getenv('TODO_idList'):
            status = "Todo"
        elif id_list == os.getenv('DOING_idList'):
            status = "Doing"
        elif id_list == os.getenv('DONE_idList'):
            status = "Done"

        return cls(trello_card["id"], trello_card["name"], trello_card["desc"], status)