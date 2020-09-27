from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import requests as Requests
import secrets

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    item_list = []
    list_id = '5f56323626c33d81cd98b386'
    r = Requests.get('https://api.trello.com/1/lists/{}/cards?key={}&token={}'.format(list_id, secrets.KEY, secrets.TOKEN))
    for items in (r.json()):
        item_list.append(items['name'])
    return render_template("index.html", items=item_list)

@app.route('/newItem', methods=['POST'])
def submitNewItem():
    item = request.form.get('itemName')
    item_list = []
    list_id = '5f56323626c33d81cd98b386'
    url = f"https://api.trello.com/1/cards"
    query = {
        'key': secrets.KEY,
        'token': secrets.TOKEN,
        'idList': list_id,
        "name": str(item)
    }
    response = Requests.request(
        "POST",
        url,
        params=query
    )
    r = Requests.get('https://api.trello.com/1/lists/{}/cards?key={}&token={}'.format(list_id, secrets.KEY, secrets.TOKEN))
    for items in (r.json()):
        item_list.append(items['name'])
    return render_template("index.html", items=item_list)

@app.route('/markAsComplete/<itemName>', methods=['POST'])
def markItemAsComplete(itemName):
    print(itemName)
    item_list = []
    list_id = '5f56323626c33d81cd98b386'
    r = Requests.get('https://api.trello.com/1/lists/{}/cards?key={}&token={}'.format(list_id, secrets.KEY, secrets.TOKEN))
    for items in (r.json()):
        if (items['name'] == itemName):
            print(items)
        item_list.append(items['name'])
    return render_template("index.html", items=item_list)    

if __name__ == '__main__':
    app.run()
