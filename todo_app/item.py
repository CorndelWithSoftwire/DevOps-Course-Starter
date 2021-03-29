class Item:
    def __init__(self, id, title, status):
        self.id = id
        self.title = title
        self.status = status

    def __repr__(self):
        return "%s, %s, %s" % (self.id, self.title, self.status)



