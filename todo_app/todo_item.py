import os
from datetime import datetime
from dateutil.parser import parse

class TodoItem:
    def __init__(self, card):
        status = ""

        if card["idList"] == os.getenv("LIST_ID_NOT_STARTED"):
            status = "Not Started"
        if card["idList"] == os.getenv("LIST_ID_IN_PROGRESS"):
            status = "In Progress"
        if card["idList"] == os.getenv("LIST_ID_DONE"):
            status = "Done"

        self.id = card["idShort"]
        self.status = status
        self.title = card["name"]
        self.last_edited = parse(card["dateLastActivity"]).replace(tzinfo=None)