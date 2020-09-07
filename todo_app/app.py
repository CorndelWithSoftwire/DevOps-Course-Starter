from flask import Flask
from flask import request
from todo_app.flask_config import Config
from flask import render_template
from todo_app.data import session_items

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/todo')
def index():
    items = session_items.get_items()
    return render_template('Index.html', items=items)

@app.route('/<id>')
def task(id):
    item = session_items.get_item(id)
    return render_template('single_item.html', item=item)

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        title = (request.form['title'])
        session_items.add_item(title)
        return index()
    else:
        return render_template('add_items.html')
    

@app.route('/index')
def yo():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
