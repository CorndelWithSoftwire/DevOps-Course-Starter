from flask import Flask, render_template, request, redirect, url_for
from todo_app.data import session_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items = session_items.get_items()
    return render_template('index.html', items=items)

@app.route('/additem', methods =["POST"])
def add_item():
    session_items.add_item(request.form.get("title"))
    return redirect(url_for("index"))
    

@app.route('/<id>')
def get_item(id):
    item = session_items.get_item(id)
    return f"Item returned is {item['title']}"





if __name__ == '__main__':
    app.run()
