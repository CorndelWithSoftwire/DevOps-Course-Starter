from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import pprint
pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index(): 
    items = session.get_items()
    return render_template('index.html' , items=items)
if __name__ == '__main__':
    app.run()

@app.route('/create', methods=['POST'])
def create():
    session.add_item(request.form.get('newItemTitle') )
    return redirect(url_for('index'), code=302)

@app.route('/view/<id>', methods=['GET'])
def view(id):
    item=session.get_item(id)
    return render_template('item.html', item=item)

@app.route('/save', methods=['POST'])
def save():
    item = { 
        'id': int(request.form.get( 'itemId' )), 
        'status': request.form.get( 'itemStatus' ), 
        'title': request.form.get( 'itemTitle' )
        }
    session.save_item( item )
    return redirect(url_for('index'), code=302) 
    
@app.route('/sort/<sortType>', methods=['GET'])
def sort_items(sortType):
    unsorted_items = session.get_items()
    pp.pprint(unsorted_items)
    sorted_items = sorted(unsorted_items, key=lambda item: item[str(sortType)].upper())
    pp.pprint(sorted_items)
    return render_template('index.html' , items=sorted_items) 

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    session.delete_item(id)
    return redirect(url_for('index'), code=302)