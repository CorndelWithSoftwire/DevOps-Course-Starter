from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    items = session.get_items()

    return  render_template("index.html",todos = items)

@app.route('/add-todo', methods = ['POST'])
def add_todo():
    item = request.form.get('name')

    session.add_item(item)

    return redirect("/")


@app.route('/delete-todo', methods = ['POST'])
def delete_todo():
        item = request.form.delete('item')

        return redirect("/")