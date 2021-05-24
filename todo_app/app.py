# SETUP INFO

from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required
from flask_login.utils import login_user
from flask_login import login_user
from oauthlib.oauth2.rfc6749.clients.base import BODY    # This line may not be required
# from flask import LoginManager and login required
import requests                     # Import the whole of requests
import json
import os        # Secrets  (local only)
import pymongo   # required for new mongo database   EXERCISE 9
from datetime import datetime, timedelta   # Needed for Mongo dates for 'older' records seperation
from todo_app.todo import User              #Import simple user class
from oauthlib.oauth2 import WebApplicationClient # Security prep work

# import pytest
from todo_app.models.view_model import ViewModel
from todo_app.todo import Todo
# from dateutil.parser import parser


app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

#################################
#  MODULE 10 LOGIN MANAGER SETUP
#################################
login_manager = LoginManager()
Clientsecurity = WebApplicationClient("7b45e6f82314a24eae60")
@login_manager.unauthorized_handler

def unauthenticated():
    print("unauthenticated, yet!") 	
    result = Clientsecurity.prepare_request_uri("https://github.com/login/oauth/authorize")
    print("The place we're about to go to is ...")
    print(result)

    return redirect(result)

		# Github OAuth flow when unauthenticated

@login_manager.user_loader
def load_user(user_id):
    return None

login_manager.init_app(app)

################################
print ("Program starting right now") 
mongopassword=os.environ["mongopassword"]           # Secure password
client_id=os.environ["client_id"]                   # For security
client_secret=os.environ["client_secret"]           # For security
#Set up variables we'll be using.
client = pymongo.MongoClient('mongodb+srv://britboy4321:' + mongopassword + '@cluster0.qfyqb.mongodb.net/myFirstDatabase?w=majority')

db = client.gettingStarted              # Database to be used
listid=os.environ["todo_listid"]
olddate = (datetime.now() - timedelta(days=5))   # Mongo: Used later to hide items older than 5 days

# olddate = (datetime.now() + timedelta(days=5))  #Uncomment this line to check 'older items'
                                                  # work without having to hang around for 5 days!

@app.route('/', methods = ["GET","PUT"])
def index():
    thislist=[]                     # Maybe can be removed           
    superlist=[]                    # Maybe can be removed
    mongosuperlist=[]               # The name of the Mongo OVERALL list with all items in it
    mongo_view_model=[]             # The name of the Mongo TO DO list (section of collection)
    mongo_view_model_doing=[]       # The name of the Mongo DOING list (section of collection)
    mongo_view_model_done=[]        # The name of the Mongo DONE list (section of collection)
    mongo_view_model_olddone=[]     # Older 'done' items to be stored here (section of collection)

    mongosuperlist = list(db.newposts.find()) 
 
#  Create the various lists depending on status
    counter=0                                           # Well, it works!
    for mongo_card in mongosuperlist:
        mongotodo = Todo.from_mongo_card(mongo_card)  # Maybe can be removed  
        
        #A list of mongo rows from the collection called 'newposts' 
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
@login_required
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


@app.route('/login/callback', methods = ["GET","POST"])
def login():
    #This is where github has it's call back sending to .. (set in github)


    #NOTES FROM INSTRUCTORS , I JUST WANT TO KEEP HERE RIGHT NOW ..
    
    # we want to call the login user function .. import from flask login
    # To read this stage we need to parse the info github has given up
   # understand what has github given us .. ask github who is the user .. 
   # github will give token .. we're gonna use that token to ask github
   # who is this
   # login that user    --- flask login library



    # Get the access_token

    url, headers, body = Clientsecurity.prepare_token_request(
        "https://github.com/login/oauth/access_token",
        authorization_response=request.url
    )
    print("REACHED HERE - CLIENT SECURITY INFO PRINTED BELOW:")
    print(Clientsecurity.prepare_token_request(
        "https://github.com/login/oauth/access_token",
        authorization_response=request.url
    ))
    
    token_response = requests.post(
        url,
        headers=headers,
        data=body,
        auth=(client_id, client_secret)
        )

    # Now to get the users data

    Clientsecurity.parse_request_body_response(token_response.text)
    url, headers, body = Clientsecurity.add_token("https://api.github.com/user")
    
    user_response = requests.get(url, headers=headers, data=body)
    # Has to be read as a JSON
    full_user_response = json.loads(user_response.text)
    # Now has to be split into individual values
    values_view = full_user_response.values()
    # Now has to be put into an interative list
    full_user_view = iter(values_view)
    # Now we need the first thing off that list, which is the user name
    the_user_name = next(full_user_view)

    # Unbelievable .. login_user won't actually accept a string it
    # will only take a user object as the first parameter, not a string
    # representing the user

    finalusername = User(the_user_name)   
    print("FINALUSERNAME IS")
    print(finalusername)
    # This printout shows:
#    FINALUSERNAME IS
#   <todo_app.todo.User object at 0x00000201093C8CA0>
# I AM 99.99% SURE THIS IS WHERE THE ISSUE IS.  LOGIN_USER IS BEING
# CALLED WITH AN INCORRECT VALUE IN finalusername.  BUT I DON'T KNOW
# HOW TO FIX IT.

    
    # I want the below kept as later may be useful for debugging

    #print("---- USER NAME ----")
    #print(the_user_name)
    #print("---- FULL USER RESPONSE ----")
    #print(full_user_response)
    #print("HTML response 200 means OK - request succeeded")
    #print("-----------------------")
    #print("URL is")
    #print(url)
    #print("headers is")
    #print(headers)
    #print("body is")
    #print(body)
    #print("-----")
    #print("Clientsecurity is")
    #print(Clientsecurity)


# *******  finalusername object has the wrong value in it, I'm 99% sure ****

    login_user(finalusername)

    return redirect("/")


if __name__ == '__main__':
   
   app.run()
