from flask import Flask, render_template, request, redirect
from todo_app.data import session_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    todo_items = session_items.get_items()
    print(todo_items) # adding this line to prove data being pulled from session items 
    return render_template('index.html', items = todo_items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    #add_todo_item = session_items.add_item(id, title, status)
    id = request.form.get('id')
    title = request.form.get('title')
    status = request.form.get('status')
    #print = "Item added " + id + " " + title + " " + status + "."
    #return render_template('index.html')
    todo_items = session_items.add_item(title) #finally display the new item
    return redirect('/')

@app.route('/item/{{ item.id }}')
def get_items(id,title,status):
    id =  get_items('id')
    return render_template('index.html', items = todo_items)
    

if __name__ == '__main__':
    app.run()
