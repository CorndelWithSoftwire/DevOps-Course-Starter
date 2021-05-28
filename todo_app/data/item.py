class Item:
    def __init__(self, id, title, status, listid):
        self.id = id
        self.title = title
        self.status = status
        self.listid= listid

    def __repr__(self):
        return "%s, %s, %s" % (self.id, self.title, self.status)

    @property
    def id(self):
        return self.id
    @id.setter
    def id(self, value):
        self.id =value

    @property
    def title(self):
        return self.title
    @id.setter
    def title(self, value):
        self.title =value

    @property
    def status(self):
        return self.status
    @id.setter
    def status(self, value):
        self.status =value
        
    @property
    def listid(self):
        return self.listid
    @id.setter
    def listid(self, value):
        self.listid =value

    



