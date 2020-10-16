from datetime import datetime

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items


    @property
    def todo_items(self):
        items = []
        for item in self._items:
            if item.status == 'Todo':
                items.append(item)
        return items

    @property
    def doing_items(self):
        items = []
        for item in self._items:
            if item.status == 'Doing':
                items.append(item)
        return items

    @property
    def done_items(self):
        items = []
        for item in self._items:
            if item.status == 'Done':
                items.append(item)
        return items

    @property
    def show_all_done_items(self):
        items = []
        for item in self._items:
            if item.status == 'Done':
                items.append(item)
        return items


    @property
    def recent_done_items(self):
        items = []
        for item in self._items:
            if item.status == 'Done':
                if item.modified_date.date() >= datetime.now().date():
                    items.append(item)
        return items
    
    @property
    def older_done_items(self):

        return items


