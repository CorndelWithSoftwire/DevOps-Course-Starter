from common import NOT_STARTED, COMPLETED


class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo(self):
        return [x for x in self._items if x.status == NOT_STARTED]

    @property
    def done(self):
        return [x for x in self._items if x.status == COMPLETED]
