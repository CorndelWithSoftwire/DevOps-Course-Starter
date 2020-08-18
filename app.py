# SETUP INFO

from flask import Flask, render_template, request, redirect, url_for
import requests                     # Import the whole of requests
import json
import session_items as session
import os        # Secrets for example Trello tokens etc in here (local only)
app = Flask(__name__)
app.config.from_object('flask_config.Config')


#Set up variables we'll be using

trellokey=os.environ["key"]            # get the secret key
trellotoken=os.environ["token"]         # get the secret token
cardsurl = "https://api.trello.com/1/cards"      # I could put the bit apart from 'cards' in some kind of 'parenturl' variable, but haven't!
acardsurl = "https://api.trello.com/1/cards/5f352898cdb592062bb71e23"                   # Used for hardcoded single card transfer from TO DO to DONE.
boardurl = "https://api.trello.com/1/boards/5f3528983d4fb244aae9f934/cards"             # The board ID is not a secret!
destinationlistid= "5f35289963b720014dd8a0ce"              # For the TO DO list and our destination for list transfer.  This is not a secret!  But is of course unique to me.  Found using postman API request,
listid = "5f352898dc8a8c31a0a1e439"                         # TO BE DONE list id - necessary for POST API CALL to add new items
donelistid = "5f3528981725711087e10339"                     # ACTUALLY DONE LIST ID

# My code deals with a maximum of 100 cards.

thislist=[]                                                                #Final list of ALL information in cards, nothing stripped out .. ready for ...
superlist=[]                                                               #Final list of actual text in cards, with rest of information stripped out .. ready for HTML
#superlist=dict()
@app.route('/', methods = ["GET","PUT"])
def index():
    # print ("Main application successfully refreshed")
    Items=session.get_items()

# Trello GET for recieving all the cards here
# First, set up the query for the board
    query = {
        'key': trellokey,
        'token': trellotoken                        # That's all I need for this API call 
    }
    response2 = requests.request(                    # Could have just used 'response' but needed a differentiator during coding. 
         "GET",
         boardurl,
         params=query
     )

 #   print(response2.text)                           # Just to check its actually being gotten!
 
    #print(response2.text)                   
    #print(type(response2.text))                     # OK so response2.text is one massive long string.  Which is fairly useless
                                                    # It was a nightmare getting the bit of the JSON I wanted
    the_list = json.loads(response2.text)           # transfer the one long string into a LIST (Not a dictionary .. pretty useless now I'm gonna have to split it by hand). I REALLY with I knew how to get it into a dictionery, would have saved hours.
#    firstcard=str(card_data[1])
#    nowsplit=firstcard.split()
    #print (nowsplit['Id'])
 #   thetype = type(card_data)
    #  print(the_list[1])                                 # Here for example is the first card details.  But still, this massive list is actually simply 1 element of a string, which is no use
                                                    # So now I need to think of some way of getting this single string into seperate elements manually
    for todo in the_list:
        superlist.append(todo["name"])                              # for each of the full cards in the list 

# I tried all the below but literally nothing would work in order to get those card id's into different parts of the list, so next tried this:
 #   counter = 0
 #   for D in thislist:
 #                                                   # We already know the key and token .. so I think query is already good.  We just have to change the URL each hit.
 #       individualCardUrl[counter]= cardsurl + "/" + (thislist[counter])
 #       print(individualCardUrl[counter])
 #       counter=counter +1
    
    # print(individualCardUrl[2])                   # ok so we have our 4 URLs built.  Now for the final loop with the GET which all needs to be put into an object ready to pass to render_template

   # counter = 0
    #for D in thislist:

     #   query = {
     #   'key': trellokey,
     #   'token': trellotoken,  
     #   'idList': thislist[counter]
     #   }

#        finalresponse[counter]=requests.request(
#            "GET",
#            individualCardUrl[counter],
#            params = query
#        )
#        counter=counter+1

# ---------------------------------------------

# CHANGE LIST THAT A CARD IS IN.   THE MVP FOR THE SPEC IS I MOVE ANY CARD FROM TO DO INTO DOING.  So this is triggered by execution (or web page refresh) and hard-code moves one of my tasks to a different list.
# This PUT should be in a different method altogether but I've spent so many hours already that I have to move forward somehow.
# 
    query = {
        'key': trellokey,
        'token': trellotoken,
        'idList': destinationlistid   
    }
    response2 = requests.request(
         "PUT",
         acardsurl,
         params=query
     )

    # Desperate to try and turn the list into a dictionery so somehow I can get HTML to print it into different lines so I can add a button against them, but it just simply isn't going to work I can only get the whole list printed as a single line in the HTML which is of course useless.

    # During module_1 a dict was returned that was in a format that somehow HTML seems to deal with.  No matter what I try I can't get 'superlist' into a format that simulates the format of the cookies list that works on the HTML.  It's too hard.  I've spent 4 hours on it.  It seems impossible with the info we have. 
    # I'm having to very deep dive the 'enumerate' and indices operations but I can't spend lots more hours in this.
    #superlist2 = {key: [index for index, x in enumerate(superlist) if x == key] for key in superlist}.  All the below fails.
    #my_dict={
    #for key in superlist:
    #    indices = []
    #    for index,value in enumerate(superlist):
    #        if value == key:
    #            indices.append(index)
    #    my_dict[key] = indices
    #print(my_dict)

    # print(superlist2)

    return render_template('index.html',passedItems=Items,todisplay=superlist)

@app.route('/addentry', methods = ["POST"])


def entry():
    # Titleback=request.form.get('title')
    # Lets try putting the Trello INSERT CARD thing in here.  First QUERY is what we're gonna send to the API
    query = {
        'key': trellokey,
        'token': trellotoken,
        'idList': listid,
        'name': request.form['title']
    }

    response = requests.request(
        "POST",
        cardsurl,
        params=query
    )


    return redirect("/")

@app.route('/complete_item', methods = ["PUT","GET","POST"])

def complete_item():

    query = {
        'key': trellokey,
        'token': trellotoken,     
        'idList': donelistid,       
        'daveurl': "https://api.trello.com/1/cards" + request.form['title2']
    }
    print(query)
    response = requests.request(
        "PUT",
        "https://api.trello.com/1/cards/" + request.form['title2'],                 # The API demands the number is put into the URL, not as part of the query
        params=query
    )

    return redirect("/")



if __name__ == '__main__':
   
#    app.run(host='http://127.0.0.1', port=port)
    app.run()
