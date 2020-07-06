
ID = 0

class Item:

    ID = 0

    def __init__(self, status, title):
        self.id = get_id()
        self.status = status
        self.title = title


    def get_id():
        ID = ID + 1
        return ID

