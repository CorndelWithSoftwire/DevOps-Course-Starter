import os

class Todo:
    def __init__(self, id, title, carddate, status="Todo"):
        self.id = id
        self.title = title
        self.status = status
        self.carddate = carddate

    @classmethod
    def from_trello_card(cls, card):
        id = card["id"]
        title = card["name"]
        status = ""
        carddate = card["dateLastActivity"]
        if card["idList"] == os.environ["todo_listid"]:
            status = "Todo"
        elif card["idList"] == os.environ["done_listid"]:
            status = "Done"
        elif card["idList"] == os.environ["doing_listid"]:
            status = "Doing"
        new_class_instance = cls(id, title, carddate, status)
        return new_class_instance
