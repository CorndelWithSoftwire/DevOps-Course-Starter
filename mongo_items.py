import requests, json, os
from item import Item
import sys
import pymongo
from datetime import datetime
from bson.objectid import ObjectId

def connect_to_mongo():
    mongo_conn = os.environ["MONGO_CONN"]
    client = pymongo.MongoClient(mongo_conn)
    database = client[os.environ["MONGO_DB_NAME"]]

    return database

def get_items():
    boardid = os.environ["MONGO_DB_NAME"]
    collections = getListsOnBoards(boardid) # get the lists on a board
    #setListIdInEnv(collections)

    items = [] 
    db = connect_to_mongo()

    for collection in collections:
        collectionsize = db[collection].count()
        cards = db[collection].find()

        for card in cards:
             item_from_list = Item.from_raw_card(card)
             items.append(item_from_list)

    return items

def getListsOnBoards(boardid):  
    # Fetch collections from database
    database = connect_to_mongo()
    collections = database.list_collection_names()
    
    return collections

def get_single_item(id):
    # Get specific card based on its ID
    items = []
    items = get_items()

    return next((items for item in items if item['id'] == id), None)
    
def add_item(title):
    # Post item and retrieve items list
    todo_list_id = os.environ["MONGO_LIST_TODO"]
    database = connect_to_mongo()
    collection = database[todo_list_id]
    doc = collection.insert_one({
        "name":title, 
        "idList":"Things To Do", 
        "dateLastActivity": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    }).inserted_id
    _id = str(ObjectId(doc))

    return _id

def remove_item(cardId):
    #Delete card 
    id = ObjectId(cardId)
    database = connect_to_mongo()
    inprogress_collection = database[os.environ["MONGO_LIST_INPROGRESS"]]
    inprogress_collection.delete_one({"_id": id})

    return True

def inprogress_item(cardId):
    #move card to Doing 
    id = ObjectId(cardId)
    database = connect_to_mongo()
    inprogress_collection = database[os.environ["MONGO_LIST_INPROGRESS"]]
    todo_collection = database[os.environ["MONGO_LIST_TODO"]]

    card = list(todo_collection.find({"_id": id}))
    insert_and_update_doc(inprogress_collection,card,id,"Doing")
    todo_collection.delete_one({"_id": id})

    return True

def markAsDone(cardId):
    # Move items marks as Done to "Done" list 
    id = ObjectId(cardId)
    database = connect_to_mongo()
    inprogress_collection = database[os.environ["MONGO_LIST_INPROGRESS"]]
    todo_collection = database[os.environ["MONGO_LIST_TODO"]]
    done_collection = database[os.environ["MONGO_LIST_DONE"]]

    todo_card = list(todo_collection.find({"_id": id}))
    inprogress_card = list(inprogress_collection.find({"_id": id}))

    if(len(todo_card) > 0):
        card = todo_card
        todo_collection.delete_one({"_id": id})
    elif(len(inprogress_card) > 0):
        card = inprogress_card
        inprogress_collection.delete_one({"_id": id})

    insert_and_update_doc(done_collection,card,id,"Done")

    return True

def insert_and_update_doc(collection,card,id,status):
    collection.insert_many(card)
    collection.find_one_and_update(
        {"_id": id},
        {"$set": {
            "idList":status,
            "dateLastActivity":datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            }
        },upsert=True
    )

def create_database(dbname):
    mongo_conn = os.environ["MONGO_CONN"]
    client = pymongo.MongoClient(mongo_conn)
    db = client[dbname]
    collection = db['test-collection']
    id = collection.insert_one({"test": 'test'})

    return id

def delete_database(dbname):
    mongo_conn = os.environ["MONGO_CONN"]
    client = pymongo.MongoClient(mongo_conn)
    client.drop_database(dbname)

    return True

def setListIdInEnv(collections):
    # Get list IDs for a Board
    for i in collections:

        # if i == "todo":
        #     os.environ["MONGODB_LIST_TODO"] = i
        # if i['name'] == "inprogress":
        #     os.environ["MONGODB_LIST_INPROGRESS"] = i['id']
        # if i['name'] == "done":
        #     os.environ["MONGODB_LIST_DONE"] = i['id']

    return 