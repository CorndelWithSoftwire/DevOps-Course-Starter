import logging

import pymongo


class MongoDatabase:
    DB_URL = None
    logger = logging.getLogger('mongo_request')
    client = None

    def getClient(self):
        if self.client is None:
            self.client = pymongo.MongoClient(self.DB_URL)
        return self.client

    def getDatabase(self):
        return self.getClient().get_database()

    def drop_database(self):
        client = self.getClient()
        client.drop_database(client.get_database())
