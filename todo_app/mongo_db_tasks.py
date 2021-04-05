import requests
import json
import os
from todo_app.Task import Task
import json
import pymongo
from bson import json_util 
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

class TasksDb:

    def get_db_name(self):  
        db_name = os.getenv('MONGO_DB_NAME') 
        if db_name is None:
            db_name = "Board"
        return db_name

    def get_tasks_db_tablename(self):  
        tasks_table_name = os.getenv('ITEMS_TABLE_NAME') 
        if tasks_table_name is None:
            tasks_table_name = "Tasks"
        return tasks_table_name

    def get_board_db(self):
        db_url = os.getenv('MONGO_DB_URL')
        if db_url is None:
            raise Exception("Environment variable MONGO_DB_URL is not set")        
        db_name = self.get_db_name()    
        client = MongoClient(db_url)
        db = client[db_name]
        return db

    def get_all_tasks(self):       
        db = self.get_board_db()        
        task_collection_name = self.get_tasks_db_tablename()
        task_collection = db[task_collection_name]
        task_list = []
        for task in task_collection.find():            
            task_list.append(Task(id=task['_id'], status=task['Status'], title=task['Title'], last_modified=task['LastModified']))
        
        return task_list

    def create_todo_task(self, title):
        db = self.get_board_db()
        task_collection_name = self.get_tasks_db_tablename()
        task_collection = db[task_collection_name]
        task = {
            "Title": title,
            "Status": "To Do",
            "LastModified":datetime.datetime.utcnow()
        }
        task_collection.insert_one(task)        

    def move_to_doing(self, id):
        self.update_status(id, "Doing")

    def move_to_done(self, id):    
        self.update_status(id, "Done")
    
    def update_status(self, id, status):    
        db = self.get_board_db()
        task_collection_name = self.get_tasks_db_tablename()
        task_collection = db[task_collection_name]    
        id_filter = { "_id": ObjectId(id) }
        newvalues = { 
            "$set": {
                "Status": status,
                "LastModified":datetime.datetime.utcnow()}        
            }    
        task_collection.update(id_filter, newvalues, upsert=True)    


    def delete_task(self, id):
        db = self.get_board_db()
        task_collection_name = self.get_tasks_db_tablename()
        task_collection = db[task_collection_name] 
        id_filter = { "_id": ObjectId(id) }
        task_collection.delete_one(id_filter)

    def get_task(self, title):
        db = self.get_board_db()
        task_collection_name = self.get_tasks_db_tablename()
        task_collection = db[task_collection_name] 
        title_filter = { "Title": title }
        return task_collection.find_one(title_filter)





headers = {
   "Accept": "application/json"
}

def get_db_name():  
    db_name = os.getenv('MONGO_DB_NAME') 
    if db_name is None:
        db_name = "Board"
    return db_name

def get_tasks_db_tablename():  
    tasks_table_name = os.getenv('TASKS_TABLE_NAME') 
    if tasks_table_name is None:
        tasks_table_name = "Tasks"
    return tasks_table_name

def get_board_db():
    db_url = os.getenv('MONGO_DB_URL')
    if db_url is None:
        raise Exception("Environment variable MONGO_DB_URL is not set")
    print(f"Database URL: {db_url}")
    db_name = get_db_name()    
    client = MongoClient(db_url)
    db = client[db_name]
    return db

def get_all_tasks():       
    db = get_board_db()        
    task_collection_name = get_tasks_db_tablename()
    task_collection = db[card_collection_name]
    tasks_list = []
    for task in task_collection.find():            
        tasks_list.append(Task(id=task['_id'], status=task['Status'], title=task['Title'], last_modified=task['LastModified']))
    
    return tasks_list

def create_todo_task(title):
    db = get_board_db()
    task_collection_name = get_tasks_db_tablename()
    task_collection = db[task_collection_name]
    task = {
        "Title": title,
        "Status": "To Do",
        "LastModified":datetime.datetime.utcnow()
    }
    task_collection.insert_one(task)        

def move_to_doing(id):
    update_status(id, "Doing")

def move_to_done(id):    
    update_status(id, "Done")
   
def update_status(id, status):    
    db = get_board_db()
    task_collection_name = get_tasks_db_tablename()
    task_collection = db[task_collection_name]    
    id_filter = { "_id": ObjectId(id) }
    newvalues = { 
        "$set": {
             "Status": status,
             "LastModified":datetime.datetime.utcnow()}        
        }    
    task_collection.update(id_filter, newvalues, upsert=True)    


def delete_task(id):
    db = get_board_db()
    task_collection_name = get_tasks_db_tablename()
    task_collection = db[task_collection_name] 
    id_filter = { "_id": ObjectId(id) }
    task_collection.delete_one(id_filter)

def get_item(title):
    db = get_board_db()
    task_collection_name = get_tasks_db_tablename()
    task_collection = db[task_collection_name] 
    title_filter = { "Title": title }
    return task_collection.find_one(title_filter)