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


@app.route('/delete-todo', methods=['POST'])
def delete_todo():
    todo_id = request.form.get('todo_id')
    session.delete_todo(todo_id)
    return redirect("/")


@app.route('/complete-todo', methods=['POST'])
def complete_todo():
    todo_id = request.form.get('todo_id')
    session.complete_todo(todo_id)
    return redirect("/")


@app.route('/started-todo', methods=['POST'])
def started_todo():
    todo_id = request.form.get('todo_id')
    session.started_todo(todo_id)
    return redirect("/")

#update function 
@app.route('/update-todo', methods=["POST"])
def update_todo():
    item = request.form.get('todo_id')
    new_todo_value = request.form.get("title")
    new_status_value = request.form.get("status")
    session.update_item(item, new_todo_value, new_status_value)
    return redirect('/')