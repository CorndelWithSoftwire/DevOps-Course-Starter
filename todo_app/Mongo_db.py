import pymongo
from mongo_config import Config
from dotenv import load_dotenv, find_dotenv

file_path = find_dotenv('.env')
load_dotenv(file_path, override=True)

def get_db(name):
    client = pymongo.MongoClient(Config.MONGO_CONNECTION)
    db = client.get_database(name)
    return db

def delete_mongo_db(name):
    """
    deletes the DB in Mongo with the given name

    Args:
        id: The name of the DB.

    Returns:
        : 
    """ 
    db = get_db(name)
    db.todo.drop()
    db.doing.drop()
    return 
