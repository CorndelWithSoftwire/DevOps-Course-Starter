from flask import Flask, render_template, request, redirect

from todo_app.flask_config import Config

import todo_app.data.session_items as session_items

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    todos = session_items.get_items()
    return render_template('index.html',todos=todos)

@app.route('/add-item', methods = ["POST"])
def add_item():
    title = request.form['title_of_todo']
    if (title != ""):
        session_items.add_item(title)
    return redirect("/")

if __name__ == '__main__':
    app.run()
