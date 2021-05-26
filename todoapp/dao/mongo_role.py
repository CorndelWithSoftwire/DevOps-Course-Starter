ROLES_COLLECTION = "roles"

class MongoGetUsers:
    def __init__(self, mongo_database):
        self._mongo_database = mongo_database

    def fetch(self):
        cursor = self._mongo_database.getDatabase()[ROLES_COLLECTION].find({})
        return list(cursor)

class MongoGetUser:
    def __init__(self, mongo_database):
        self._mongo_database = mongo_database

    def fetch(self, user_id):
        user = self._mongo_database.getDatabase()[ROLES_COLLECTION].find_one({ "id" : user_id })
        return user

class MongoAddUser:
    def __init__(self, mongo_database):
        self._mongo_database = mongo_database

    def add(self, id, role):
        try:
            self._mongo_database.getDatabase()[ROLES_COLLECTION].insert_one({ "id" : id , "role" : role } )

        except Exception as err:
            self._mongo_database.logger.error(f'Other error occurred: {err}')
            raise Exception("Request failed. See logs.")


class MongoUpdateRole:
    def __init__(self, mongo_database):
        self._mongo_database = mongo_database

    def update(self, id, role):
        try:
            self._mongo_database.getDatabase()[ROLES_COLLECTION].update_one({"id": id}, { "$set": { "role": role } })

        except Exception as err:
            self._mongo_database.logger.error(f'Other error occurred: {err}')
            raise Exception("Request failed. See logs.")


class MongoDeleteUser:
    def __init__(self, mongo_database):
        self._mongo_database = mongo_database

    def delete(self, user_id):
        try:
            self._mongo_database.getDatabase()[ROLES_COLLECTION].delete_one({"id": user_id})

        except Exception as err:
            self._mongo_database.logger.error(f'Other error occurred: {err}')
            raise Exception("Request failed. See logs.")

