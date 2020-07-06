from flask import Flask, render_template, request, redirect, url_for
#from config import TRELLO_URL
import config as cf

import session_items as session
import requests


app = Flask(__name__)
app.config.from_object('flask_config.Config')
#load_dotenv()

@app.route('/')
def index():
    items = session.get_items()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def addToDo():
    title = request.form['title']
    session.add_item(title)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()


"""
Add a complete_item route that accepts the ID of an item as a
parameter and then calls a method to change its status from 'To
Do' to 'Done'
curl -i "localhost:5000/api/foo?a=hello&b=world" 
"""
@app.route('/complete_item/<idCard>', methods=['PUT'])
def update_card(idCard):

    idCustomField = 'status'
    data = {'value' : 'Done'}
    url = f"https://api.trello.com/1/cards/{idCard}/customField/{idCustomField}/item"
    
    query = cf.get_trello_query()
    response = requests.request("PUT", url, data, params=query)
    print(response.text)

#create card/item
def add_card():
    url = "https://api.trello.com/1/cards"
    
    query = cf.get_trello_query()
    #No obvious way of retrieving the created List Id, 
    #therefore reusing/mocking the example one instead 
    query['idList'] = '5abbe4b7ddc1b351ef961414'
    response = requests.request("POST", url, params=query )
    print(response.text)

#Fetch Cards on a list
def get_cards(id):
    url = f"https://api.trello.com/1/lists/{id}/cards"
    
    query = cf.get_trello_query()    
    response = requests.request("GET", url, params=query)
    print(response.text)


# create list
def add_list_to_board(name):
    url = "https://api.trello.com/1/lists"
    query = cf.get_trello_query()
    
    query['name'] = 'MyCorndelDevOpsToDoBoard'
    #No obvious way of retrieving the created Board Id, 
    #therefore reusing/mocking the example one instead 
    query['idBoard'] = '5abbe4b7ddc1b351ef961414'

    response = requests.request( "POST", url, params=query )
    print(response.text)


#Create New Board
def create_to_do_board():

    url = "https://api.trello.com/1/boards/"
    query = cf.get_trello_query()
    query['name'] = 'MyCorndelDevOpsToDoBoard'

   response = requests.request(  "POST", url, params=query )
   print(response.text)

