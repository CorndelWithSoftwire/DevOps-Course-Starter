import jsons
from bson import ObjectId

from todoapp.common import *
from todoapp.mongo_database import MongoDatabase


class MongoGetCards():
    def __init__(self, mongo_database, status_to_list_map):
        self._mongo_database = mongo_database
        self._status_to_list_map = status_to_list_map

    def fetchForList(self, id_list):
        cursor = self._mongo_database.getDatabase()[id_list].find({})
        return list(cursor)


class MongoAddCard():
    def __init__(self, mongo_database, listId):
        self._mongo_database = mongo_database
        self.listId = listId

    def add(self, item):
        try:
            self._mongo_database.logger.info(f"Mongo add card: {item}")
            self._mongo_database.getDatabase()[self.listId].insert_one(jsons.dump(item))

        except Exception as err:
            self._mongo_database.logger.error(f'Other error occurred: {err}')
            raise Exception("Request failed. See logs.")


class MongoUpdateCard():
    def __init__(self, mongo_database):
        self._mongo_database = mongo_database

    def update(self, id, old_list, new_list):
        try:
            self._mongo_database.logger.info(f"Mongo update card: [{id}] from [{old_list}] to [{new_list}]")
            item = self._mongo_database.getDatabase()[old_list].find_one_and_delete({"_id": ObjectId(id)})
            self._mongo_database.getDatabase()[new_list].insert_one(item)

        except Exception as err:
            self._mongo_database.logger.error(f'Other error occurred: {err}')
            raise Exception("Request failed. See logs.")


class MongoDeleteCard():
    def __init__(self, mongo_database, status_to_list_map):
        self._mongo_database = mongo_database
        self._status_to_list_map = status_to_list_map

    def delete(self, cardId):
        try:
            self._mongo_database.logger.info(f"Mongo delete card: {cardId}")
            for value in self._status_to_list_map.values():
                self._mongo_database.getDatabase()[value].delete_one({"_id" : ObjectId(cardId)})

        except Exception as err:
            self._mongo_database.logger.error(f'Other error occurred: {err}')
            raise Exception("Request failed. See logs.")

class MongoBoard():

    def fetchLists(self):
        return Lists.TODO_LIST_NAME, Lists.DONE_LIST_NAME

