import os

class TodoItem:
    def __init__(self, id, name, id_list):
        self.id = id
        self.title = name
        self.status = ""

        if id_list == os.getenv('TRELLO_TODO_LIST'):
            self.status = "To Do"
        elif id_list == os.getenv('TRELLO_IN_PROGRESS_LIST'):
            self.status = "In Progress"
        elif id_list == os.getenv('TRELLO_COMPLETED_LIST'):
            self.status = "Done"