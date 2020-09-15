class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def todo_items(self):
        todo_items = []
        
        for item in self._items:
            if item.status == "Todo":
                todo_items.append(item)

        return todo_items

    @property
    def done_items(self):
        done_items = []
        
        for item in self._items:
            if item.status == "Done":
                done_items.append(item)

        return done_items