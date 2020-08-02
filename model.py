
#ID = 0

class Item:

    ID = 0

    def __init__(self, status, title):
        self.id = Item.ID + 1
        self.status = status
        self.title = title


