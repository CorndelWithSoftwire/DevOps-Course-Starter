class Item(object):
    def __init__(self, id, cardID, status, title, listId):
        self._id = id
        self._cardID = cardID
        self._status = status
        self._title = title
        self._listId = listId
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def cardID(self):
        return self._cardID

    @cardID.setter
    def cardID(self, value):
        self._cardID = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    
    @property
    def listId(self):
        return self._listId
    
    @listId.setter
    def listId(self, value):
        self._listId = value