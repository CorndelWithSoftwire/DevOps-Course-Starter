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

@app.route('/markAsComplete/<item_id>')
def markAsComplete(item_id):
    print(item_id)
    item_list = []
    list_id = '5f56323626c33d81cd98b386'
    r = Requests.get('https://api.trello.com/1/lists/{}/cards?key={}&token={}'.format(list_id, secrets.KEY, secrets.TOKEN))
    items_list = r.json()
    item_key = ''
    for item in items_list:
        if (item['name'] == item_id):
            item_key = item['id']
    print("Item Key: {}", item_key)
    list_to_move_to = '5f56324465484e35d83eb45b'
    url = Requests.put('https://api.trello.com/1/cards/{}?key={}&token={}&idList={}'.format(item_key, secrets.KEY, secrets.TOKEN, list_to_move_to))
    print("Json")
    print(url.text)
    return render_template("index.html", items=item_list)    

if __name__ == '__main__':
    app.run()
