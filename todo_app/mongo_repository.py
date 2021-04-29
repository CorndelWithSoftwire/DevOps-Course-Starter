from datetime import datetime
from pprint import pprint

import pymongo
from bson import ObjectId
from pymongo import ReturnDocument

from todo_app.flask_config import Config
from todo_app.item import Status, Item


class MongoRepository:
    def __init__(self):
        self.config = Config()
        mongo_client = pymongo.MongoClient(self.config.MONGO_URL)
        self.db = mongo_client[self.config.MONGO_DB_NAME]
        self.todo_collection = self.db[self.config.MONGO_LIST_COLLECTION]

    def add_item(self, tittle, description):
        list_item = {
            'name': tittle,
            'desc': description,
            'status': Status.NOT_STARTED.name,
            'dateLastActivity': datetime.now(),
        }
        saved_list = self.todo_collection.insert_one(list_item)
        pprint(f'Saved item with id = ${saved_list.inserted_id} to list collection')

    def get_items(self):
        items = []
        for doc in self.todo_collection.find():
            items.append(Item.from_response(doc))

        return items

    def move_to_done(self, item_id):
        saved = self.todo_collection.find_one_and_update({'_id': ObjectId(item_id)},
                                                         {'$set': {'status': 'COMPLETED'}},
                                                         return_document=ReturnDocument.AFTER)
        pprint(f'item with id = ${item_id} moved to done')
