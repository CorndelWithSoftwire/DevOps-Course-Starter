from datetime import datetime

class Item:

    #def __init__(self, id, status, title, _date = datetime.today().date()):
    def __init__(self, id, status, title, _date = datetime.now().strftime('%Y-%m-%d')):
        self.id = id
        self.status = status
        self.title = title
        self._date = _date


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

    #show_all_done_items
    @property
    def doneItems(self):
        return self.getItems('Done')
    
    #recent_done_items
    @property
    def recent_done_items(self):
        itemsList = list()
        for item in self.doneItems:
            done_date_str = item._date[:10]
            print(done_date_str)
            done_date = self.get_date_from_str(done_date_str)
            #done_date = datetime.fromisoformat(done_date_str).date()
            if done_date == datetime.today().date():
                itemsList.append(item)
        return itemsList

    #older_done_items
    @property
    def older_done_items(self):
        itemsList = list()
        for item in self.doneItems:
            done_date_str = item._date[:10]
            print(done_date_str)
            done_date = self.get_date_from_str(done_date_str)
            #done_date = datetime.fromisoformat(done_date_str).date()
            if done_date < datetime.today().date():
                itemsList.append(item)
        return itemsList

    def getItems(self, _status):
        itemsList = list()
        for item in self._items:
            if item.status == _status:
                itemsList.append(item)

        return itemsList

    def get_date_from_str(self, _str):
        #return datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ')
        return datetime.strptime(_str, '%Y-%m-%d').date()

    def repr(self):
        pass
