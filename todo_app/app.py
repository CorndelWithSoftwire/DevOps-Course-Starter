from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config

from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', todoList = get_items())

@app.route('/new_todo', methods=['POST'])
def add_item_from_form():
    title = request.form['title']
    add_item(title)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
