from flask import Flask, render_template, request, redirect, url_for, session
import session_items as session
import ItemsViewModel as ItemsViewModel

app = Flask(__name__)
app.config.from_object('flask_config.Config')

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('flask_config.Config')

#     # All the routes and setup code etc
#     return app

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
    # Get ToDo items
    thingstodo = ItemsViewModel.ItemsViewModel(items)
    thingstodo.get_item_thingstodo()
   
    # Get Doing items
    doing = ItemsViewModel.ItemsViewModel(items)
    doing.get_item_doing()

    # Get ALL Done items
    done_all = ItemsViewModel.ItemsViewModel(items)
    done_all.show_all_done_items()

    # Get all Done items completed TODAY
    done_today = ItemsViewModel.ItemsViewModel(items)
    done_today.recent_done_items()

    #  # Get ALL Done items completed before today
    done_older = ItemsViewModel.ItemsViewModel(items)
    done_older.older_done_items()

    return render_template('index.html', thingstodo=thingstodo, doing=doing, done_all=done_all, done_older=done_older, done_today=done_today)

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

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

if __name__ == '__main__':
    app.run()

