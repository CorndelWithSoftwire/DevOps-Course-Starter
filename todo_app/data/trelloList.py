class TrelloList(object):
    def __init__(self, boardId, name):
        self._boardId = boardId
        self._name = name
    
    @property
    def boardId(self):
        return self._boardId

    @boardId.setter
    def boardId(self, value):
        self._boardId = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value