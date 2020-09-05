from flask import Flask, request, render_template
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item, get_item, save_item, delete_item
from operator import itemgetter

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items = get_items()
    ##renders the template with the items sorted by status
    return render_template('index.html',items=sorted(items,key=itemgetter('status'), reverse=True))

@app.route('/add_todo_item', methods=['POST']) 
def add_todo_item(): 
    new_todo_item = request.form.get('newitem', "")
    add_item(new_todo_item)
    items = get_items()
    ##renders the template with the items sorted by status
    return render_template('index.html',items=sorted(items,key=itemgetter('status'),reverse=True))

@app.route('/completed', methods=['POST']) 
def completed(): 
    ##retrieve the id of the completed task
    completed_item = request.values.get('id')
    ##retrieve the item of the completed task
    item = get_item(completed_item)
    ##create a new dictionary item that will be used to overwrite the existing value 
    updated_item = { 'id': item['id'],  'status': 'Completed', 'title': item['title']}
    
    ##overwrite the dictionary item with the new value containing a status of completed
    save_item(updated_item)
    ##retrieve the items
    items = get_items()
    
    ##renders the template with the items sorted by status
    return render_template('index.html',items=sorted(items,key=itemgetter('status'),reverse=True))


@app.route('/delete', methods=['POST']) 
def delete(): 
    ##retrieve the id of the item to delete
    target_item_id = request.values.get('id')
    ##retrieve the item of the completed task
    item = get_item(target_item_id)   
    ##overwrite the dictionary item with the new value containing a status of completed
    delete_item(item)
    ##retrieve the items
    items = get_items()
    
    ##renders the template with the items sorted by status
    return render_template('index.html',items=sorted(items,key=itemgetter('status'),reverse=True))


if __name__ == '__main__':
    app.run()
