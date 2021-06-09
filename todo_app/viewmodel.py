import requests, datetime

class ViewModel:
    def __init__(self, items):
        self._items = items
    @property
    def items(self):
        return self._items
    @property
    def todoitems(self):
        todo_items = [item for item in self._items if item.status == 'To Do']        
        return todo_items
    @property
    def doingitems(self):
        doing_items = [item for item in self._items if item.status == 'Doing']        
        return doing_items
    @property
    def show_all_done_items(self):
        all_done_items = [item for item in self._items if item.status == 'Done']        
        return all_done_items
    @property
    def recent_done_items(self):
        all_done_items = [item for item in self._items if item.status == 'Done']
        today = datetime.datetime.utcnow()
        recent_done_items = [item for item in all_done_items if item.lastmodifieddate.date() >= today.date()]    
        return recent_done_items
    @property
    def older_done_items(self):
        all_done_items = [item for item in self._items if item.status == 'Done']
        today = datetime.datetime.utcnow() 
        older_done_items = [item for item in all_done_items if item.lastmodifieddate.date() < today.date()]    
        return older_done_items     