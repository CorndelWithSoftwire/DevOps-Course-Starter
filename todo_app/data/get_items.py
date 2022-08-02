class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        todo_list_items = []     
        for item in self.items:
            if item.status == 'To Do':
                todo_list_items.append(item)
        return todo_list_items

    @property
    def done_items(self):
        done_list_items = []     
        for item in self.items:
            if item.status == 'Done':
                done_list_items.append(item)
        return done_list_items

