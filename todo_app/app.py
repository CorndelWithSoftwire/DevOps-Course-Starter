from flask import Flask, render_template, request, redirect, url_for
import data.session_items as session
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        item_title = request.form['Title']
        session.add_item(item_title)
        return redirect('/')
    else:
        items_list = session.get_items()
        # print(items_list)
        return render_template('index.html', items_list=items_list)


if __name__ == '__main__':
    app.run()
