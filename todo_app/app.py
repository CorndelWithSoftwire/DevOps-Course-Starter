from flask import Flask, render_template, request,session

from todo_app.flask_config import Config

import session_items

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        title = request.form['title_of_todo']
        if (title != ""):
            session_items.add_item(title)
        #return 'Hello World!'
    todos = session_items.get_items()
    return render_template('index.html',todos=todos)


if __name__ == '__main__':
    app.run()
