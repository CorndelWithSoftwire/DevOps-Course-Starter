from datetime import datetime
import iso8601

class ViewModel(object):
    items = []

    def __init__(self, items):
        """
        docstring
        """
        self.items = items

    @property
    def todo_items(self):
        return list(filter(lambda item: containsStatus(item, "To Do"), self.items))

    @property
    def all_items(self):
        return self.items

    @property
    def doing_items(self):
        return list(filter(lambda item: containsStatus(item, "Doing"), self.items))

    @property
    def done_items(self):
        return list(filter(lambda item: containsStatus(item, "Done"), self.items))

    @property
    def all_done_items(self):
        items = list(filter(lambda item: containsStatus(item, "Done"), self.items))
        if len(items) >= 5:
            return sorted(items, key = lambda item: item.lastActivity, reverse=True)[:5]
        else:
            return sorted(items, key = lambda item: item.lastActivity, reverse=True)

    @property
    def recent_done_items(self):
        now = datetime.now()
        items = list(filter(lambda item: containsStatus(item, "Done") and item.lastActivity.date() == now.date(), self.items))
        if len(items) == 0:
            return []
        else:
            return sorted(items, key = lambda item: item.lastActivity, reverse=True)

def containsStatus(element, status):
    if type(element).__name__ == 'Item':
        return element.status == status
    else:
        return False