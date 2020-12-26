from flask import Flask,render_template, redirect, request

from todo_app.flask_config import Config

from todo_app.data import session_items

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items = session_items.get_items()
    return render_template('index.html',items = items)

@app.route('/additem', methods=["POST"])
def add_item():
    title = request.form['title']
    session_items.add_item(title)
    return redirect('/')

if __name__ == '__main__':
    app.run()
