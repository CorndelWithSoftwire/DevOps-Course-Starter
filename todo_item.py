import os

class TodoItem:
    def __init__(self, id, title, status):
        self.id = id
        self.title = title
        self.status = status

    @classmethod
    def from_trello_card(cls, trello_card):
        id = trello_card["id"]
        title = trello_card["name"]
        status = ""

        if trello_card["idList"] == os.getenv('NOT_STARTED'):
            status = "Not Started"
        elif trello_card["idList"] == os.getenv('IN_PROGRESS'):
            status = "In Progress"
        elif trello_card["idList"] == os.getenv('COMPLETED'):
            status = "Completed"

        return cls(id, title, status)

