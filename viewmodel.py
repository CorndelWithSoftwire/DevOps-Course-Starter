from datetime import datetime

from common import NOT_STARTED, COMPLETED

MAX_DONE_SHOWN = 5


class ViewModel:
    def __init__(self, items):
        self._items = items
        self._done = [x for x in self._items if x.status == COMPLETED]

    @property
    def items(self):
        return self._items

    @property
    def todo(self):
        return [x for x in self._items if x.status == NOT_STARTED]

    @property
    def done(self):
        return self._done

    @property
    def show_all_done_items(self):
        return len(self._done) < MAX_DONE_SHOWN

    @property
    def recent_done_items(self):
        todays_date = datetime.today().date()
        return [x for x in self._done if x.last_modified.date() == todays_date]

    @property
    def older_done_items(self):
        todays_date = datetime.today().date()
        return [x for x in self._done if x.last_modified.date() != todays_date]
