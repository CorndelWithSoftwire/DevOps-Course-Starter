import os.path
from flask import Flask,escape,request,Response,render_template
import todo_app.data.session_items as session

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def index():
    items = session.get_items()
    return render_template("./index.html", items=items)


if __name__ == '__main__':
    app.debug = True
    app.run()
