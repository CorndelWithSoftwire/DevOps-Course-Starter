from flask import Flask, render_template, request, redirect, url_for
import Trello_items as trello
import requests

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    items = trello.get_items_trello()
    items=sorted(items, key=lambda k: k['status'], reverse=True)
    return render_template('index.html', items=items)

@app.route('/<id>/completed', methods=['POST'])
def completeditem(id):
    trello.save_item_trello(id)
    return redirect('/') 

@app.route('/newitems', methods=['POST'])
def newitems():
    itemname = request.form.get('Title')
    trello.add_item_trello(itemname)
    return redirect('/') 

if __name__ == '__main__':
    app.run()
