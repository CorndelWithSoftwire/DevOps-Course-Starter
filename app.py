from trello import TrelloClient
from flask import Flask, render_template, request, redirect, url_for
import requests
import json

url = "https://api.trello.com/b/DxTGbmpc/to-do"

headers = {"Accept": "application/json"}
query = {'key': '6f90eb6475d80df64613af31f4a74a28',
   'token': '1015b49a51dc7965ab53b695d0a6e9ce10c93356fbbbc4a2a5d36b362aeeb4d3'
}

response = requests.request.get("https://api.trello.com/b/DxTGbmpc/to-do")
print(json.dumps(json.loads(response.text)


#import session_items as session
app = Flask(__name__)
app.config.from_object('flask_config.Config')
if __name__ == "__main__":
    app.run(debug=True)


#update from work 2.0
@app.route('/')
def index():
    items = session.get_items()
    return render_template('index.html', todos = items)
    
@app.route('/add-todo', methods=["POST"])
def add_todo():
    item = request.form.get('todo_task')
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
    new_todo_value = request.form.get("title")
    new_status_value = request.form.get("status")
    session.update_item(item, new_todo_value, new_status_value)
    return redirect('/')