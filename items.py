class Items:

    def __init__(self, id, title, dateLastActivity, status ):
        self.id = id
        self.title = title
        self.status = status
        self.dateLastActivity = dateLastActivity


    def get_items(self):    
        itemslist = []
        itemslist = { 'id': self.id , 'title': self.title, 'dateLastActivity': self.dateLastActivity, 'status': self.status }
        return itemslist