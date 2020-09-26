
class Item:

    def __init__(self, id, status, title):
        self.id = id
        self.status = status
        self.title = title


class ViewModel:
    
    def __init__(self, items):
        self._items = items
        
    @property
    def items(self):
        return self._items 