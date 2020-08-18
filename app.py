from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/')
def index(name=None):
    return render_template('index.html', items=session.get_items())


@app.route('/', methods=["POST"])
def additem():
    NewToDoItem = request.form["NewToDoItem"]
    session.add_item(NewToDoItem)
    return render_template('index.html', items=session.get_items())


if __name__ == '__main__':
    app.run()
