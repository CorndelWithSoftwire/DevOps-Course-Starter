import pymongo
#from mongo_config import Config
#from dotenv import load_dotenv, find_dotenv

#file_path = find_dotenv('.env')
#load_dotenv(file_path, override=True)

from Mongo_items import client

def delete_mongo_db(name):
    """
    deletes the DB in Mongo with the given name

    Args:
        id: The name of the DB.

    Returns:
        : 
    """
    #mongologin = Config.MONGO_USER + ':' + Config.MONGO_PASS + "@" + Config.MONGO_URL 
    #client = pymongo.MongoClient("mongodb+srv://" + mongologin + "/" + Config.MONGO_NAME + "?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true")
    db = client.get_database(name)
    #db.collection.delete_one({})
    #db.todo.drop()
    #db.doing.drop()
    return 
