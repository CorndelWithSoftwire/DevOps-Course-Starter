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

def mark_done_item_doing_mongo(id):
    """
    sets an existing done item in mongo to the doing collection and deletes from the done collection

    Args:
        item: The ID of the item to update.
    """
    done = db.done
    doing = db.doing
    doing.insert_one(done.find_one({"_id" : ObjectId(id) })).inserted_id
    done.delete_one(done.find_one({"_id" : ObjectId(id) }))

def mark_todo_item_done_mongo(id):
    """
    sets an existing todo in mongo to the done collection and deletes from the todo collection

    Args:
        item: The ID of the item to update.
    """
    todo = db.todo
    done = db.done
    done.insert_one(todo.find_one({"_id" : ObjectId(id) })).inserted_id
    todo.delete_one(todo.find_one({"_id" : ObjectId(id) }))

def mark_doing_item_done_mongo(id):
    """
    sets an existing doing item in mongo to the done collection and deletes from the doing collection

    Args:
        item: The ID of the item to update.
    """
    done = db.done
    doing = db.doing
    done.insert_one(doing.find_one({"_id" : ObjectId(id) })).inserted_id
    doing.delete_one(doing.find_one({"_id" : ObjectId(id) }))





#add_item_mongo("todo_item_done")
#mark_todo_item_doing_mongo("609d43d9f69eaec5f040b4c3")
#mark_done_item_doing_mongo("60916afb46d633ac495437b3")
#mark_todo_item_done_mongo("609d48b25a29536c2b6d32b0")
#mark_doing_item_done_mongo("60916ac16b039134c61377f1")
