from flask import Flask, render_template, request, redirect, url_for, session
import session_items as session
import ItemsViewModel as ItemsViewModel

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    return redirect('tasks')

@app.route('/clearsession')
def clearsession():
    session.clearsessions()
    return render_template("index.html")

@app.route('/tasks')
def list_tasks():
    items = session.get_items()
    thingstodo = ItemsViewModel.ItemsViewModel(items)
    thingstodo.get_item_thingstodo()
    done = ItemsViewModel.ItemsViewModel(items)
    done.get_item_done()
    doing = ItemsViewModel.ItemsViewModel(items)
    doing.get_item_doing()
    return render_template('index.html', thingstodo=thingstodo, done=done, doing=doing)

@app.route('/tasks', methods=['POST'])
def post_item():
    
    form = request.form
    complete = False
    remove = False
    id = 0

    # Take ID from form and split by _ to get item ID
    for key in form:
        #print(key)
        if key.startswith('Done_'):
            complete = True
            id = key.partition('_')[-1]
            
        if key.startswith('Remove_'):
            remove = True
            id = key.partition('_')[-1]
    
    # If new item added
    if "addtask" in form:
         tasktitle = request.form['addtask']
         if(tasktitle != ''):
            session.add_item(tasktitle)
         items = session.get_items()

    # If item marked as Done
    if complete:
        session.markAsDone(id)
        items = session.get_items()

    # If item marked as Remove
    if remove:  
        session.remove_item(id)
        items = session.get_items()

    else:
        items = session.get_items()
    
    

    return render_template("index.html", items=items)
    #return render_template("index.html")

@app.route('/tasks/<id>', methods=['GET'])
def get_item(id):
    singleitem = session.get_item(id)
    print(singleitem)
    return render_template("index.html", singleitem=singleitem)



if __name__ == '__main__':
    app.run()

