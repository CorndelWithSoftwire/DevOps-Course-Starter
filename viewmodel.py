from item import Item


class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        todo_items = list(filter(lambda item: item.status == Item.STATUS_NOT_STARTED, self._items))
        return todo_items

    @property
    def done_items(self):
        done_items = list(filter(lambda item: item.status == Item.STATUS_COMPLETED, self._items))
        return done_items
