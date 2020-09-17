import os

class Card:
    def __init__(self, id, name, desc, id_list):
        self.id = id
        self.name = name
        self.desc = desc

        if id_list == os.getenv('TODO_idList'):
            self.status = "Todo"
        elif id_list == os.getenv('DOING_idList'):
            self.status = "Doing"
        elif id_list == os.getenv('DONE_idList'):
            self.status = "Done"
    
    def is_done(self):
        return self.status == "Done"
