import os

class TodoItem:
    def __init__(self, id, status, title):
        self.id = id
        self.status = status
        self.title = title

    @classmethod
    def from_raw_trello_card(cls, card):
        id = card["id"]
        title = card["name"]
        status = ""

        if card["idList"] == os.getenv("TODO_LIST_ID"):
            status = "To Do"
        elif card["idList"] == os.getenv("DONE_LIST_ID"):
            status = "Done"
        elif card["idList"] == os.getenv("DOING_LIST_ID"):
            status = "Doing"

        return cls(id, status, title)

     