from flask import Flask, render_template
from todo_app.flask_config import Config

from todo_app.data.session_items import get_items

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', todoList = get_items())


if __name__ == '__main__':
    app.run()
