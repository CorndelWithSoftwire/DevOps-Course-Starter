from flask import Flask, render_template, request, redirect, url_for
import session_items as session
from flask import request

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    items = session.get_items()
    return render_template('index.html', items = items)

@app.route('/add_Item', methods=['POST'])
def add_Item():
    item = request.form['title']
    session.add_item(item)

    return 'Added Successfully!'

if __name__ == '__main__':
    app.run()
