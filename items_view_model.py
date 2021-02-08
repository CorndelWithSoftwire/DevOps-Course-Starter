from datetime import datetime

class ItemsViewModel:

    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items
    
    @property
    def todo_items(self):
        filteredItems = []
        for x in self._items:
            if x.status == "Things To Do":
                filteredItems.append(x)
        return filteredItems
    
    @property
    def doing_items(self):
        filteredItems = []
        for x in self._items:
            if x.status == "Doing":
                filteredItems.append(x)
        return filteredItems

    @property
    def done_items(self):
        filteredItems = []
        for x in self._items:
            if x.status == "Done":
                filteredItems.append(x)
        return filteredItems

    @property
    def show_all_done_items(self):
        return len(self.done_items) < 5
        
    @property
    def recent_done_items(self): 
        filteredItems = []
        for x in self.done_items:
            if x.datetime.date() == datetime.today().date():
                filteredItems.append(x)
        return filteredItems

    @property
    def older_done_items(self): 
        filteredItems = []
        for x in self.done_items:
            if x.datetime.date() < datetime.today().date():
                filteredItems.append(x)
        return filteredItems