from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():    
    items = session.get_items()
    return  render_template("index.html",todoitems=items)#'Hello World!'

if __name__ == '__main__':
    app.run()

@app.route('/', methods=['POST'])
def add_item():   
    strtitle = request.form.get('title')#request.form['title']  
    if strtitle!='':
        session.add_item(strtitle)
    return redirect('/')
    
@app.route('/<id>')
def complete_item(id):   
    strlist=session.get_item(id)
    strlist['status']="Completed"
    session.save_item(strlist)    
    return redirect('/')  

@app.route('/remove/<id>')
def delete_item(id):   
    session.remove_item(id)           
    return redirect('/')  

@app.route('/clear')
def reinitialize_list():
    session.clear_items()
    return redirect('/')  

   