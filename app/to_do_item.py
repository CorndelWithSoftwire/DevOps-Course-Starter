from datetime import datetime


class ToDoItem(object):
    def __init__(self, id:str, status:str, title:str, last_modified:datetime):
        self.id = id
        self.status = status
        self.title = title
        self.last_modified = last_modified

    def __str__(self):
        return self.title+'-'+self.status+'-'+self.last_modified
        