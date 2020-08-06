from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

#changed to the template for local host v2.0

#update from work 2.0

@app.route('/')
def index():
    items = session.get_items()
    print (items)
    print ("===========items")

    return render_template('index.html', todos = items)
    
@app.route('/add-todo', methods=["POST"])
def add_todo():
    item = request.form.get('todo')
    print(item)

    session.add_item(item)

    return redirect('/')

#delete function 
@app.route('/delete-todo', methods=["POST"])
def delete_todo():
    item = request.form.get('todo_id')
    print(item)

    session.delete_item(item)

    return redirect('/')

#update function 
@app.route('/update-todo', methods=["POST"])
def update_todo():
    item = request.form.get('todo_id')
    new_todo_value = request.form.get("todo_value")
    print(item)

    session.update_item(item, new_todo_value)

    return redirect('/')