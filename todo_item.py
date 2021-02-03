import os

class TodoItem:
    def __init__(self, id, name, idList):
        self.id = id
        self.title = name
        self.status = ""

        if idList == os.getenv('NOT_STARTED'):
            self.status = "Not Started"
        elif idList == os.getenv('IN_PROGRESS'):
            self.status = "In Progress"
        elif idList == os.getenv('COMPLETED'):
            self.status = "Completed"
