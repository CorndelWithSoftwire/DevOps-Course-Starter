import os
from datetime import datetime
import dateutil.parser

NOT_STARTED = 'Not Started'
COMPLETED = 'Completed'


class Lists:
    TODO_LIST_NAME = "Todo"
    DONE_LIST_NAME = "Done"

    def __init__(self, todo_list_id, done_list_id):
        self.list_id_map = {
            self.TODO_LIST_NAME : todo_list_id,
            self.DONE_LIST_NAME : done_list_id
        }

    @property
    def todo_list_id(self):
        return self.list_id_map[self.TODO_LIST_NAME]

    @property
    def done_list_id(self):
        return self.list_id_map[self.DONE_LIST_NAME]

    @property
    def status_to_list_map(self):
        return {
            NOT_STARTED: self.todo_list_id,
            COMPLETED: self.done_list_id
        }

    @property
    def list_to_status_map(self):
        return {
            self.todo_list_id: NOT_STARTED,
            self.done_list_id: COMPLETED
        }


class TodoItem:
    def __init__(self, title, status, id=None, duedate=None, last_modified=datetime.now().isoformat()):
        self.last_modified = dateutil.parser.parse(last_modified)
        self.id = id
        self.title = title
        self.status = status
        self.duedate = duedate
