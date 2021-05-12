
from flask import Flask, render_template, request, redirect, url_for, session
from todo_app.data import session_items

from todo_app.flask_config import Config
from todo_app.data.trello import Trello
import requests
import os


#def create_app():
app = Flask(__name__)
app.config.from_object(Config)
secret_key = os.getenv('SECRET_KEY')
    # All the routes and setup code etc
  #  return app


trello=Trello()

@app.route('/')
def index():
    
  #Call trello.py get cards from List
    items = trello.getCardsfromList()
    return render_template('index.html', items=items)
    # item_view_model = ViewModel(items)
    # render_template('index.html',view_model=item_view_model)
    

@app.route('/additem', methods =["POST"])
def add_item():
    trello.addCardtodoList(request.form.get('title'))
    return redirect(url_for("index"))
    
@app.route('/movecarddoing', methods =["POST"])
def move_carddoing():
    trello.moveCardfromtodoListdoing(request.form.get('id'))
    return redirect(url_for("index"))
    
@app.route('/movecarddone', methods =["POST"])
def move_carddone():
    trello.moveCardfromtodoListdone(request.form.get('id'))
    return redirect(url_for("index"))

@app.route('/deletecard', methods =["POST"])
def deletecard():
    trello.deleteCard(request.form.get('id'))   
    return redirect(url_for("index"))

# @app.route('/boardid', methods =["GET"])
# def getboardid()
#   #Call trello.py get cards from List
#     listitems = trello.getboardid()
#     return render_template('index.html', items=listitems)
    

if __name__ == '__main__':
    app.run()
