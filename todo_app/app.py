# SETUP INFO

from flask import Flask, render_template, request, redirect, url_for
import requests                     # Import the whole of requests
import json
import os        # Secrets for example Trello tokens etc in here (local only)
import pymongo   # required for new mongo database   EXERCISE 9
from datetime import datetime, timedelta   # Needed for Mongo dates for 'older' records seperation

# import pytest
from todo_app.models.view_model import ViewModel
from todo_app.todo import Todo
# from dateutil.parser import parser

app = Flask(__name__)
print ("Program starting now") 
mongopassword=os.environ["mongopass"]           # Secure password
#Set up variables we'll be using.
client = pymongo.MongoClient('mongodb+srv://britboy4321:' + mongopassword + '@cluster0.qfyqb.mongodb.net/myFirstDatabase?w=majority')
db = client.gettingStarted              # Database to be used
listid=os.environ["todo_listid"]
olddate = (datetime.now() - timedelta(days=5))   # Mongo: Used later to hide items older than 5 days

# olddate = (datetime.now() + timedelta(days=5))  #Uncomment this line to check 'older items'
                                                  # work without having to hang around for 5 days!

@app.route('/', methods = ["GET","PUT"])
def index():
    thislist=[]                  
    superlist=[] 
    mongosuperlist=[]               # The name of the Mongo OVERALL list with all items in it
    mongo_view_model=[]             # The name of the Mongo TO DO list (section of collection)
    mongo_view_model_doing=[]       # The name of the Mongo DOING list (section of collection)
    mongo_view_model_done=[]        # The name of the Mongo DONE list (section of collection)
    mongo_view_model_olddone=[]     # Older 'done' items to be stored here (section of collection)

    mongosuperlist = list(db.newposts.find()) 
 
#  Create the various lists depending on status
    counter=0                                           # Well, it works!
    for mongo_card in mongosuperlist:
        mongotodo = Todo.from_mongo_card(mongo_card)    #A list of mongo rows from the collection called 'newposts' 
        whatsthestatus=(mongosuperlist[counter]['status'])
        whatsthedate=(mongosuperlist[counter]['mongodate'])      # Need the date to seperate older 'Done'
        counter=counter+1                                   #Increment as need to get next list item
        if whatsthestatus == "todo":
            mongo_view_model.append(mongo_card)             # Append to the todo
        elif whatsthestatus == "doing":
            mongo_view_model_doing.append(mongo_card)       # Append to doing
        elif whatsthestatus == "done":
            if whatsthedate > olddate:
                mongo_view_model_done.append(mongo_card)        # Append to display in done - recently
            else: 
                mongo_view_model_olddone.append(mongo_card)     # Apprend to display in older done record
                  
                                                            # note: Invalid or no status won't appear at all

    return render_template('index.html', 
    passed_items_todo=mongo_view_model,             # Mongo To Do
    passed_items_doing=mongo_view_model_doing,      # Mongo Doing
    passed_items_done=mongo_view_model_done,        # Mongo Done
    passed_items_olddone=mongo_view_model_olddone   # Old items ready to be displayed elsewhere
    )

@app.route('/addmongoentry', methods = ["POST"])
def mongoentry():
    name = request.form['title']
    mongodict={'title':name,'status':'todo', 'mongodate':datetime.now()}
    db.newposts.insert(mongodict)
    return redirect("/")

@app.route('/move_to_doing_item', methods = ["PUT","GET","POST"])

def move_to_doing_item():           # Called to move a 'card' to 'doing'
    title = request.form['item_title']
    myquery = { "title": title }
    newvalues = { "$set": { "status": "doing" } }
    db.newposts.update_one(myquery, newvalues)
    for doc in db.newposts.find():  
      print(doc)
    return redirect("/")

@app.route('/move_to_done_item', methods = ["PUT","GET","POST"])
def move_to_done_item():            # Called to move a 'card' to 'done'
  
    title = request.form['item_title']
    myquery = { "title": title }
    newvalues = { "$set": { "status": "done" } }
    db.newposts.update_one(myquery, newvalues)
    for doc in db.newposts.find():  
      print(doc)
    return redirect("/")


@app.route('/move_to_todo_item', methods = ["PUT","GET","POST"])
def move_to_todo_item():            # Called to move a 'card' BACK to 'todo' (was useful)
    title = request.form['item_title']
    myquery = { "title": title }
    newvalues = { "$set": { "status": "todo" } }
    db.newposts.update_one(myquery, newvalues)
    for doc in db.newposts.find():  
      print(doc)
    return redirect("/")

if __name__ == '__main__':
   
   app.run()
