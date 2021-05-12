class ViewModel:
    def __init__(self,items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todoitems(self):
        items = []
        for item in self._items:
            print(item)
            #if item's status is 'ToDo' then
            if item.status == 'ToDo':
                # add item to items array (items.insert(1, item)
                items.insert(1, item)
            
        return items 

    @property
    def doingitems(self):
        return []