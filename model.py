
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

    @property
    def todoItems(self):
        return self.getItems('To Do')
        
    @property
    def doingItems(self):
        return self.getItems('Doing')

    @property
    def doneItems(self):
        return self.getItems('Done')

    def getItems(self, _status):
        itemsList = list()
        for item in self._items:
            if item.status == _status:
                itemsList.append(item)

        return itemsList
