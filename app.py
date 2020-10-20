from flask import Flask, render_template, request, redirect, url_for
import Trello_items as trello
import requests, datetime

app = Flask(__name__)
app.config.from_object('flask_config.Config')

class ViewModel:
    def __init__(self, items):
        self._items = items
    @property
    def items(self):
        return self._items
    @property
    def todoitems(self):
        todo_items = [item for item in self._items if item.status == 'To Do']        
        return todo_items
    @property
    def doingitems(self):
        doing_items = [item for item in self._items if item.status == 'Doing']        
        return doing_items
    @property
    def show_all_done_items(self):
        all_done_items = [item for item in self._items if item.status == 'Done']        
        return all_done_items
    @property
    def recent_done_items(self):
        all_done_items = [item for item in self._items if item.status == 'Done']
        today = datetime.date.today()
        recent_done_items = [item for item in all_done_items if item.lastmodifieddate >= today]    
        return recent_done_items
    @property
    def older_done_items(self):
        all_done_items = [item for item in self._items if item.status == 'Done']
        today = datetime.date.today()
        older_done_items = [item for item in all_done_items if item.lastmodifieddate < today]    
        return older_done_items

@app.route('/')
def index():
    items = trello.get_items_trello()
    items=sorted(items, key=lambda k: k.status, reverse=True)
    item_view_model = ViewModel(items)
    return render_template('index.html', view_model=item_view_model)
    #return render_template('index.html', items=items)

@app.route('/<id>/completed', methods=['POST'])
def completeditem(id):
    trello.mark_item_done_trello(id)
    return redirect('/') 

@app.route('/<id>/todo', methods=['POST'])
def todoitem(id):
    trello.mark_item_todo_trello(id)
    return redirect('/') 

@app.route('/<id>/doing', methods=['POST'])
def doingitem(id):
    trello.mark_item_doing_trello(id)
    return redirect('/') 

@app.route('/newitems', methods=['POST'])
def newitems():
    itemname = request.form.get('Title')
    trello.add_item_trello(itemname)
    return redirect('/') 

if __name__ == '__main__':
    app.run()
