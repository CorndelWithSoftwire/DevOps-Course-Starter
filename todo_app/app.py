from flask import Flask
from flask import render_template

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
