from flask import Flask,request,render_template, redirect
import todo_app.data.session_items as session
from todo_app.flask_config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/add_item')
def add_item():
    title = request.args.get('name')
    session.add_item(title)
    return redirect("/")

@app.route('/')
def index():
    items = session.get_items()
    return render_template("index.html", items=items)


if __name__ == '__main__':
    app.run()
