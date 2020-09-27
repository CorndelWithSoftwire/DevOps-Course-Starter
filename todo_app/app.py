from flask import Flask
from flask import render_template,request,redirect
from .data.session_items import *

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

#web pages
@app.route('/')
def index():
    return render_template('index.html',items=get_items())

@app.route('/<id>')
def getitem(id):
    return render_template('item.html',item=get_item(id))

#post methods
@app.route('/newitem',methods=["POST"])
def newitem():
    add_item(request.form['title'])
    return redirect('/')

@app.route('/<id>/edit',methods=["POST"])
def edititem(id):
    item = get_item(id)
    item['title'] = request.form['title']
    item['status'] = request.form['statusRadio']
    save_item(item)
    return redirect('/')

@app.route('/<id>/delete',methods=["POST"])
def deleteitem(id):
    del_item(id)
    return redirect('/')

if __name__ == '__main__':
    app.run()
