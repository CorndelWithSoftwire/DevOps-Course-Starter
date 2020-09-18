from flask import Flask,render_template,url_for,redirect,request
from todo_app.data import session_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

##@app.route('/')
##def root():
##    return redirect(url_for('index'))
 
@app.route('/Add', methods=['POST'])
def add_new():
    title = request.form["title"]   
    new_item = session_items.add_item(title)
    return redirect(url_for('index'))

##  if request.method == 'POST':
##        new_item = session_items.add_item('Title')
##    else:
##        items = session_items.get_items()
##        return ender_template('index.html',items=items)

@app.route('/UpdateToDone',methods=['GET'])
def update():
    id = int(request.args['id'])
    session_items.UpdateToDone(id)
    return redirect(url_for('index'))


@app.route('/')
def index():
    items = session_items.get_items()
    ##new_item = session_items.add_item('Title') ## new line
    return render_template('index.html',items=items)
    

if __name__ == '__main__':
    app.run()
