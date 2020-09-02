class ItemsViewModel:

    def __init__(self, items):
        self._items = items
        #self._status = status

    @property
    def items(self):
        return self._items

    def get_item_done(self):
        filteredItems = []
        for x in self._items:
            if x['status'] == "Done":
                filteredItems.append(x)
        self._items = filteredItems
        return self._items
    
    def get_item_thingstodo(self):
        filteredItems = []
        for x in self._items:
            if x['status'] == "Things To Do":
                filteredItems.append(x)
        self._items = filteredItems
        return self._items
    
    def get_item_doing(self):
        filteredItems = []
        for x in self._items:
            if x['status'] == "Doing":
                filteredItems.append(x)
        self._items = filteredItems
        return self._items