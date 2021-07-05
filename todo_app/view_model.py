from datetime import datetime, timedelta


class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        todo_items = []
        for item in self._items:
            if item.status == "To Do":
                todo_items.append(item)
        return todo_items

    @property
    def in_progress_items(self):
        in_progress_items = []
        for item in self._items:
            if item.status == "In Progress":
                in_progress_items.append(item)
        return in_progress_items

    @property
    def complete_items(self):
        complete_items = []
        for item in self._items:
            if item.status == "Complete":
                complete_items.append(item)
        return complete_items

    @property
    def show_all_done_items(self):
        if len(self.complete_items) <= 5:
            return True
        else:
            return False

    @property
    def recent_done_items(self):
        datetime_yesterday = datetime.now() - timedelta(days=1)
        recent_done_items = []
        for item in self._items:
            if (item.status == "Complete") and (item.last_edited > datetime_yesterday):
                recent_done_items.append(item)

        return recent_done_items

    @property
    def older_done_items(self):
        datetime_yesterday = datetime.now() - timedelta(minutes=1)
        older_done_items = []
        for item in self._items:
            if (item.status == "Complete") and (item.last_edited < datetime_yesterday):
                older_done_items.append(item)
            
        return older_done_items
