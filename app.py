from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    items = session.get_items()
    session.add_item('Avi')
    return render_template("index.html", items=items)


@app.route('/', methods=['POST'])
def create():
    items = session.get_items()
    session.add_item(request.form.get('item_title'))
    return render_template("index.html", items=items)


if __name__ == '__main__':
    app.run()
