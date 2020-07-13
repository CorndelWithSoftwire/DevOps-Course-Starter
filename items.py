class Items:

    def __init__(self, id, title, status ):
        self.id = id
        self.title = title
        self.status = status


    def get_items(self):    
        itemslist = []
        itemslist = { 'id': self.id , 'title': self.title, 'status': self.status }
        return itemslist