from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import requests
from secrets import KEY, TOKEN

app = Flask(__name__)
app.config.from_object('flask_config.Config')

def get_items_trello():
    apiurl = "https://api.trello.com/1/"
    boardsurl = "boards/5f6076c34c5f48265943e31e/"
    cardsurl = "cards/"
    query = {'key' : KEY, 'token' : TOKEN}
    cards = requests.get(apiurl+boardsurl+"cards", params=query)
    cards_json = cards.json()

    items = []
    for card in cards_json:
        cardlist = requests.get(apiurl+cardsurl+card['id']+"/list", params=query)
        cardlist_json = cardlist.json()
        if cardlist_json['name'] == 'Done':
            cardstatus = 'Completed'
        else :
            cardstatus = cardlist_json['name'] 
        items.append({"id" : card['id'], "status": cardstatus, "title": card['name']})
    return items

@app.route('/')
def index():
    items = get_items_trello()
    items=sorted(items, key=lambda k: k['status'], reverse=True)
    return render_template('index.html', items=items)

def save_item_trello(id):
    url = "https://api.trello.com/1/cards/" + id
    query = {'key' : KEY, 'token' : TOKEN, "idList": "5f6076e96994a166c05385a6"}
    requests.put(url, params=query)
    return id

#route to allow updating of status for each item based on id number
@app.route('/<id>/completed', methods=['POST'])
def completeditem(id):
    save_item_trello(id)
    return redirect('/') 

def add_item_trello(title):
    url = "https://api.trello.com/1/cards/"
    query = {'key' : KEY, 'token' : TOKEN, "idList": "5f6076e68cc021208da06d2b", "name" : title}
    requests.post(url, params=query)
    return 

@app.route('/newitems', methods=['POST'])
def newitems():
    itemname = request.form.get('Title')
    add_item_trello(itemname)
    return redirect('/') 

if __name__ == '__main__':
    app.run()
