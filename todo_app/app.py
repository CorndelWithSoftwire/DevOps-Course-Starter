from flask import Flask, render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data import session_items as session

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
