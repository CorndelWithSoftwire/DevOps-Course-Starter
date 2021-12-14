from flask import Flask, render_template, url_for, request, session

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template("index.html")
