from flask import Flask, render_template, request
from todo_app.flask_config import Config
from todo_app.data.session_items import *

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html', items = get_items())

@app.route('/add', methods=['POST'])
def add():
    add_item(request.form.get('title'))
    return render_template('index.html', items = get_items())

@app.route('/setstatus/<id>/<status>', methods=['POST'])
def setstatus(id,status):
    item = get_item(id)
    item['status'] = status
    save_item(item)
    return render_template('index.html', items = get_items())

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    item = get_item(id)
    delete_item(item)
    return render_template('index.html', items = get_items())

if __name__ == '__main__':
    app.run()
