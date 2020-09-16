from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import requests
from secrets import KEY, TOKEN

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    apiurl = "https://api.trello.com/1/"
    boardsurl = "boards/5f6076c34c5f48265943e31e/"
    cardsurl = "cards/"
    query = {'key' : KEY, 'token' : TOKEN}
    cards = requests.get(apiurl+boardsurl+"cards", params=query)
    cards_json = cards.json()

    items = []
    for card in cards_json:
        trellocard = requests.get(apiurl+cardsurl+card['id']+"/list", params=query)
        trellocard_json = trellocard.json()
        if trellocard_json['name'] == 'Done':
            cardstatus = 'Completed'
        else :
            cardstatus = trellocard_json['name'] 
        items.append({"id" : card['id'], "status": cardstatus, "title": card['name']})
    items=sorted(items, key=lambda k: k['status'], reverse=True)
    return render_template('index.html', items=items)

#route to allow updating of status for each item based on id number
@app.route('/<id>/completed', methods=['POST'])
def completeditem(id):
    #populate variable with the relevant item
    item = session.get_item(id)
    item['status']='Completed'
    session.save_item(item)
    #return user to index page
    return redirect('/') 


@app.route('/newitems', methods=['POST'])
def newitems():
    #capture the title of newitem using a form and pass it to the add_item function
    session.add_item(request.form.get('Title')) 
    #redirect to index page
    return redirect('/') 

if __name__ == '__main__':
    app.run()
