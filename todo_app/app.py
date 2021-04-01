# SETUP INFO - this it the one

from flask import Flask, render_template, request, redirect, url_for
import requests                     # Import the whole of requests
import json
import os        # Secrets for example Trello tokens etc in here (local only)
import pymongo   # required for new mongo database   EXERCISE 9
from datetime import datetime, timedelta   # Needed for Mongo dates

# import pytest
from todo_app.models.view_model import ViewModel
from todo_app.todo import Todo
# from dateutil.parser import parser

app = Flask(__name__)
print ("Program starting now") 

#Set up variables we'll be using

trellokey=os.environ["key"]            # get the secret key
trellotoken=os.environ["token"]         # get the secret token
mongo_username="britboy4321"              # to be put into secrets later, not used right now
mongo_password="Mongodbpass"              # to be put into secrets later, not used right now
client = pymongo.MongoClient("mongodb+srv://britboy4321:Mongodbpass@cluster0.qfyqb.mongodb.net/myFirstDatabase?w=majority")
db = client.gettingStarted              # Database to be used
listid=os.environ["todo_listid"]
cardsurl = "https://api.trello.com/1/cards"
olddate = (datetime.now() - timedelta(days=5))   # Used later to hide items older than 5 days

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
    mongo_view_model_olddone=[]   # Older 'done' items
    cardsurl = "https://api.trello.com/1/cards"      
    boardurl = f"https://api.trello.com/1/boards/{os.environ['board_id']}/cards"             # The board ID is not a secret!

# Trello GET for recieving all the cards here

    query = {
        'key': trellokey,
        'token': trellotoken                
    }
    board_response = requests.request(                     
         "GET",
         boardurl,
         params=query
     )


    # db.newposts.remove()    # Emergency wipeout all Mongo data here if needed USE WITH CAUTION!

    # dave = client.list_database_names     #  WORKS - good test
    mongosuperlist = list(db.newposts.find()) 
 

#  Create the various lists depending on status
    counter=0                   # Well, it works!
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
                mongo_view_model_olddone.append(mongo_card)  
                  
                  
                                                            # note: Invalid or no status won't appear at all


# Keep the trello list for the moment
    card_list = json.loads(board_response.text)     # A list of cards TRELLO 
    for trello_card in card_list:
        todo = Todo.from_trello_card(trello_card)
        superlist.append(todo)
    item_view_model = ViewModel(superlist)


    return render_template('index.html', 
    view_model=item_view_model,                     # The trello list
    passed_items_todo=mongo_view_model,             # Mongo To Do
    passed_items_doing=mongo_view_model_doing,      # Mongo Doing
    passed_items_done=mongo_view_model_done,        # Mongo Done
    passed_items_olddone=mongo_view_model_olddone   # Old items ready to be displayed elsewhere
    )


@app.route('/addentry', methods = ["POST"])
def entry():
    query = {
        'key': trellokey,
        'token': trellotoken,
        'idList': listid,
        'name': request.form['title']
    }

    response = requests.post(
        cardsurl,
        params=query
    )
    return redirect("/")

@app.route('/addmongoentry', methods = ["POST"])
def mongoentry():

# 'name': request.form['title']

    name = request.form['title']
    mongodict={'title':name,'status':'todo', 'mongodate':datetime.now()}
    # olddate=(datetime.now()-5)
    # print(datetime.now())
    db.newposts.insert(mongodict)


    return redirect("/")



# A trello complete action
@app.route('/complete_item', methods = ["PUT","GET","POST"])

def complete_item():
    done_listid = "5f3528981725711087e10339"
    id = request.form['item_id']
    query = {
        'key': trellokey,
        'token': trellotoken,
        'idList' : done_listid   
    }
    response = requests.request(
        "PUT",
        "https://api.trello.com/1/cards/" + id,
        params=query
    )
    return redirect("/")


# MONGO move item to 'doing'

@app.route('/move_to_doing_item', methods = ["PUT","GET","POST"])

def move_to_doing_item():
    # update 'row' sent from collection, set status = "doing"
    title = request.form['item_title']
    myquery = { "title": title }
    newvalues = { "$set": { "status": "doing" } }
    db.newposts.update_one(myquery, newvalues)
    for doc in db.newposts.find():  
      print(doc)
    return redirect("/")

@app.route('/move_to_done_item', methods = ["PUT","GET","POST"])
def move_to_done_item():
  
    title = request.form['item_title']
    myquery = { "title": title }
    newvalues = { "$set": { "status": "done" } }
    db.newposts.update_one(myquery, newvalues)
    for doc in db.newposts.find():  
      print(doc)
    return redirect("/")


@app.route('/move_to_todo_item', methods = ["PUT","GET","POST"])
def move_to_todo_item():
    title = request.form['item_title']
    myquery = { "title": title }
    newvalues = { "$set": { "status": "todo" } }
    db.newposts.update_one(myquery, newvalues)
    for doc in db.newposts.find():  
      print(doc)
    return redirect("/")











    


if __name__ == '__main__':
   
   app.run()
