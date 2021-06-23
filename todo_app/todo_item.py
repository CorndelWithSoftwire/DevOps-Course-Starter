import os
from datetime import datetime
from dateutil.parser import parse


class TodoItem:
    def __init__(self, card):
        status = ""

        if card["idList"] == os.getenv("to_do_list"):
            status = "To Do"
        if card["idList"] == os.getenv("in_progress_list"):
            status = "In Progress"
        if card["idList"] == os.getenv("complete_list"):
            status = "Complete"

        self.id = card["idShort"]
        self.status = status
        self.title = card["name"]
        self.last_edited = parse(card["dateLastActivity"]).replace(tzinfo=None)
        self.due_date = (
            (parse(card["due"]).replace(tzinfo=None)).strftime("%d-%B-%Y")
            if type(card["due"]) == str
            else "No due date set"
        )
