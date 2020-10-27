from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        item_title = request.form['Title']
        add_item(item_title)
        return redirect('/')
    else:
        items_list = get_items()
        return render_template('index.html', items_list=items_list)


if __name__ == '__main__':
    app.run()
