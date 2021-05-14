import requests, pymongo, pprint
import os, datetime
from mongo_config import Config
from bson.objectid import ObjectId



mongologin = Config.MONGO_USER + ':' + Config.MONGO_PASS + "@" + Config.MONGO_URL 


client = pymongo.MongoClient("mongodb+srv://" + mongologin + "/" + Config.MONGO_DB_NAME + "?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true")

db = client.test_database

collection = db.test_collection


class Item:
    def __init__(self, id, title, lastmodifieddate, status='To Do'):
        self.id = id
        self.status = status
        self.title = title
        self.lastmodifieddate = lastmodifieddate


def get_items_mongo():
    """
    Fetches all cards from Mongo DB.

    Returns:
        list: The list of saved items.
    """   
    items = []
    todo = db.todo
    doing = db.doing
    done = db.done
    for item in todo.find():
        items.append(Item(item['_id'], item['title'], item['lastmodifieddate'],"To Do"))
    for item in doing.find():
        items.append(Item(item['_id'], item['title'], item['lastmodifieddate'],"Doing"))
    for item in done.find():
        items.append(Item(item['_id'], item['title'], item['lastmodifieddate'],"Done"))        
    return items



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
    return

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
    return

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
    return

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
    return

def mark_done_item_todo_mongo(id):
    """
    sets an existing done item in mongo to the todo collection and deletes from the done collection

    Args:
        item: The ID of the item to update.
    """
    todo = db.todo
    done = db.done
    todo.insert_one(done.find_one({"_id" : ObjectId(id) })).inserted_id
    done.delete_one(done.find_one({"_id" : ObjectId(id) }))
    return

def mark_doing_item_todo_mongo(id):
    """
    sets an existing doing item in mongo to the todo collection and deletes from the doing collection

    Args:
        item: The ID of the item to update.
    """
    todo = db.todo
    doing = db.doing
    todo.insert_one(doing.find_one({"_id" : ObjectId(id) })).inserted_id
    doing.delete_one(doing.find_one({"_id" : ObjectId(id) }))
    return
