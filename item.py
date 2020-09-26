from enum import Enum, auto

from flask_config import Config


class Item:
    def __init__(self, item_id, tittle, status, desc):
        self.title = tittle
        self.status = status
        self.id = item_id
        self.desc = desc

    @staticmethod
    def from_response(response):
        r_title = response['name']
        r_status = Status.COMPLETED if Config.DONE_LIST_ID == response['idList'] else Status.NOT_STARTED
        r_id = response['id']
        r_desc = response['desc']
        return Item(r_id, r_title, r_status, r_desc)


class Status(Enum):
    COMPLETED = auto()
    NOT_STARTED = auto()
