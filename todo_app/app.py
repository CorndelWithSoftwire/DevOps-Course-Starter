from flask import Flask, render_template, redirect, request, Response
import todo_app.data.session_items as session
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items_list = session.get_items()
    return render_template("index.html", items = items_list)

@app.route('/addItem', methods =["POST"])
def add():
    title = request.form.get('new_todo_item')
    session.add_item(title)
    return redirect ("/")

@app.route('/completeItem/<id>', methods =["POST"])
def complete_item(id):
    converted_id = int(id)
    item = session.get_item(converted_id)
    item["status"] = "Completed"
    session.save_item(item)
    return redirect ("/")

if __name__ == '__main__':
    app.run()

