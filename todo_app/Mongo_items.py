import requests, pymongo, pprint
import os, datetime
from todo_app.mongo_config import Config
from bson.objectid import ObjectId



mongologin = Config.MONGO_USER + ':' + Config.MONGO_PASS + "@" + Config.MONGO_URL 


client = pymongo.MongoClient("mongodb+srv://" + mongologin + "/" + os.environ.get('MONGO_DB_NAME') + "?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")

db = client.test_database

collection = db.test_collection

#item1 = {"author": "Kev","text": "My Test","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}

def add_item_mongo(title):
    """
    Adds a new item with the specified title to the Mongo DB.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    newitem = {'title' : title, "lastmodifieddate" : datetime.datetime.utcnow()}
    todo = db.todo
    todo.insert_one(newitem).inserted_id
    return 

def mark_todo_item_doing_mongo(id):
    """
    sets an existing todo in mongo to the doing collection and deletes from the todo collection

    Args:
        item: The ID of the item to update.
    """
    todo = db.todo
    doing = db.doing
    doing.insert_one(todo.find_one({"_id" : ObjectId(id) })).inserted_id
    todo.delete_one(todo.find_one({"_id" : ObjectId(id) }))


#add_item_mongo("brand_new_mongo_item")
#mark_todo_item_doing_mongo("609d43d9f69eaec5f040b4c3")