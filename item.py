from datetime import date, datetime
from enum import Enum, auto

from flask_config import Config


class Item:
    def __init__(self, item_id, tittle, status, desc, last_changed=date.today()):
        self.title = tittle
        self.status = status
        self.id = item_id
        self.desc = desc
        self.last_changed = last_changed

    @staticmethod
    def from_response(response):
        config = Config()
        r_title = response['name']
        r_status = Status.COMPLETED if config.DONE_LIST_ID == response['idList'] else Status.NOT_STARTED
        r_id = response['id']
        r_desc = response['desc']
        datestr = response['dateLastActivity'].split('T')[0]
        r_last_changed = datetime.fromisoformat(datestr).date()
        return Item(r_id, r_title, r_status, r_desc, r_last_changed)


class Status(Enum):
    COMPLETED = auto()
    NOT_STARTED = auto()
