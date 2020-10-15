from flask import Flask, render_template, request, redirect, url_for
import Trello_items as trello
import requests

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
        todo_items = [item for item in self._items if item['status'] == 'to do']        
        return todo_items

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

@app.route('/newitems', methods=['POST'])
def newitems():
    itemname = request.form.get('Title')
    trello.add_item_trello(itemname)
    return redirect('/') 

if __name__ == '__main__':
    app.run()
