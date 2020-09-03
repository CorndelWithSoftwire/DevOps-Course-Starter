from flask import Flask
from todo_app.flask_config import Config
from flask import render_template
import things



app = Flask(__name__)
app.config.from_object(Config)
tasks = [{'id': 1, 'title': 'test'}, {'id': 2, 'title': 'testing'}, {'id': 3, 'title': 'tester'}]

@app.route('/id')
def index(id):
    items = get_item(id)
    return render_template('Index.html', items=items)

@app.route('/index')
def yo():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
