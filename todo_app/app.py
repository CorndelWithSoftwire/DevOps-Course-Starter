from flask import Flask
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
    items = session_items.get_item(id)
    return render_template('Index.html', items=items)

@app.route('/index')
def yo():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
