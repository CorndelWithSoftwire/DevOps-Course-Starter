from flask import Flask, render_template, request, redirect,url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import add_item, get_items

app = Flask(__name__)
app.config.from_object(Config())
    

@app.route('/')
def index():
    #return 'Hello World!'
    items = get_items()
    return render_template('index.html', items1=items)


@app.route('/addItem', methods=['POST'])
def addNewItems():
    newitem1 = request.form.get('newItem') 
    items = add_item(newitem1)
    return redirect(url_for('index'))  
    pass



