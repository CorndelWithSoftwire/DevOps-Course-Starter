from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    todo=session.get_items()
    return render_template('index.html',all_todo=todo)

@app.route('/', methods=["POST"])
def add_todo():
    td_new_title=request.form.get('td_Title')
    if (len(td_new_title) > 1 ):
        session.add_item(td_new_title)
    return index()
#    todo=session.get_items()
#    return render_template('index.html',all_todo=todo)

@app.route('/del', methods=['POST']) 
def del_book():     
# Code to create a new book entry in the database. 
    return render_template('message.html')

if __name__ == '__main__':
    app.run()
