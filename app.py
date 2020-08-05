from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

#changed to the template for local host v2.0

#update from work 2.0

@app.route('/')
def index():
    items = session.get_items()

    return render_template('index.html', todos = items)
    
@app.route('/add-todo', methods=["POST"])
def add_todo():
    item = request.form.get('name')

    session.add_item(item)

    return redirect('/')

