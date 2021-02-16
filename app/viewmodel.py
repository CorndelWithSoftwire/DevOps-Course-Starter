from datetime import datetime, date
from typing import List
from app.to_do_item import ToDoItem

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def to_do(self):
        return [item for item in self._items if item.status == "To Do"]

    @property
    def doing(self):
        return [item for item in self._items if item.status == "Doing"]

    @property
    def done(self):
        return [item for item in self._items if item.status == "Done"]

    @property
    def show_all_done_items(self):
        if len(self.done) < 5:
            return self.done
        else:
            return self.recent_done_items

    @property
    def recent_done_items(self):
        today:date = datetime.now().date()

        done_items:List[ToDoItem] = self.done

        filtered_done_items = filter(lambda item: item.last_modified.date() == today , done_items)

        return list(filtered_done_items)

    @property
    def older_done_items(self):
        today:date = datetime.now().date()

        done_items:List[ToDoItem] = self.done

        filtered_done_items = filter(lambda item: item.last_modified.date() != today , done_items)

        return list(filtered_done_items)
