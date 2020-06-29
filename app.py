from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/tasks')
def list_tasks():
    items = session.get_items()
    return render_template("index.html", items=items)

@app.route('/tasks', methods=['POST'])
def post_item():
    
    form = request.form
    complete = False
    remove = False
    id = 0

    for key in form:
        print(key)
        if key.startswith('Done_'):
            complete = True
            id = key.partition('_')[-1]
            
        if key.startswith('Remove_'):
            remove = True
            id = key.partition('_')[-1]
            
    if "addtask" in form:
         tasktitle = request.form['addtask']
         if(tasktitle != ''):
            session.add_item(tasktitle)
         items = session.get_items()

    if complete:
        print("Raj Done " + str(id))
        print(id)
        items = session.get_items()

    if remove:  
        print("Raj Remove " + str(id))
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

