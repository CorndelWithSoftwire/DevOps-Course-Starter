from flask import Flask, render_template, request, redirect, url_for
from session_items import get_items

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', list=items)

if __name__ == '__main__':
    app.run()
