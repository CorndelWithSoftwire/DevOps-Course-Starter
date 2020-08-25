from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    #populate variable with the list of saved todo items
    items = session.get_items()
    #sort the list ased on the value of the status field in reverse order
    items=sorted(items, key=lambda k: k['status'], reverse=True)
    #pass the sorted list into the index template for display
    return render_template('index.html', items=items)

#route to allow updating of status for each item based on id number
@app.route('/<id>', methods=['POST'])
def item(id):
    #populate variable with the relevant item
    item = session.get_item(id)
    #Check current status, update and then save accordingly
    if item['status']=='Not Started':
        item['status']='Complete'
        session.save_item(item)
    elif item['status']=='Complete':
        item['status']='Not Started'
        session.save_item(item)
    #return user to index page
    return redirect('/') 


@app.route('/newitems', methods=['POST'])
def newitems():
    #capture the title of newitem using a form and pass it to the add_item function
    session.add_item(request.form.get('Title')) 
    #redirect to index page
    return redirect('/') 

if __name__ == '__main__':
    app.run()
