# Constants
import os

TODO_LIST_ID = os.getenv("TODO_LIST_ID")
DONE_LIST_ID = os.getenv("DONE_LIST_ID")

NOT_STARTED = 'Not Started'
COMPLETED = 'Completed'

STATUS_TO_LIST_MAP = {
    NOT_STARTED: TODO_LIST_ID,
    COMPLETED: DONE_LIST_ID
}

LIST_TO_STATUS_MAP = {
    TODO_LIST_ID: NOT_STARTED,
    DONE_LIST_ID: COMPLETED
}


class TodoItem:
    def __init__(self, title, status, id=None, duedate=None):
        self.id = id
        self.title = title
        self.status = status
        self.duedate = duedate