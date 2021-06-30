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
            if item.status == "Not Started":
                todo_items.append(item)

        return todo_items

    @property
    def doing_items(self):
        doing_items = []
        for item in self._items:
            if item.status == "In Progress":
                doing_items.append(item)

        return doing_items

    @property
    def done_items(self):
        done_items = []
        for item in self._items:
            if item.status == "Done":
                done_items.append(item)

        return done_items

    @property
    def show_all_done_items(self):
        if len(self.done_items) <= 5:
            return True
        else:
            return False

    @property
    def recent_done_items(self):
        datetime_yesterday = datetime.now() - timedelta(days=1)
        recent_done_items = []
        for item in self._items:
            if (item.status == "Done") and (item.last_edited > datetime_yesterday):
                recent_done_items.append(item)

        return recent_done_items

    @property
    def older_done_items(self):
        datetime_yesterday = datetime.now() - timedelta(days=1)
        older_done_items = []
        for item in self._items:
            if (item.status == "Done") and (item.last_edited < datetime_yesterday):
                older_done_items.append(item)
     
        return older_done_items
