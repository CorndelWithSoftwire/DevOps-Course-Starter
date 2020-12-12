  
from flask import Flask
from flask import render_template,redirect,request

from todo_app.flask_config import Config
from todo_app.data.classes import *

app = Flask(__name__)
app.config.from_object(Config)
trello = Trello(Config)


# web pages
@app.route('/')
def index():
    lists = [List(k,i) for i,k in enumerate(trello.get_lists())]
    cards = [Card(lists,i) for i in trello.get_cards()]
    card_view_model = ViewModel(cards,lists)
    return render_template('index.html',card_view_model=card_view_model)

@app.route('/card/<id>')
def getitem(id):
    lists = [List(k,i) for i,k in enumerate(trello.get_lists())]
    card = Card(lists,trello.get_card(id))
    card_view_model = ViewModel(card,lists)
    return render_template('editCard.html',card_view_model=card_view_model)

# post methods
@app.route('/card/newcard',methods=["POST"])
def newitem():
    lists = [List(k,i) for i,k in enumerate(trello.get_lists())]
    name = request.form['name']
    desc = request.form['desc']
    due = request.form['due']
    trello.add_card(lists,name,desc,due)
    return redirect('/')

@app.route('/card/<id>/editcard',methods=["POST"])
def editcard(id):
    name = request.form['name']
    desc = request.form['desc']
    due = request.form['due']
    idList = request.form['statusRadio']
    trello.save_card(id,name,desc,due,idList)
    return redirect('/')

@app.route('/card/<id>/deletecard',methods=["POST"])
def deleteitem(id):
    trello.delete_card(id)
    return redirect('/')

if __name__ == '__main__':
    app.run()
