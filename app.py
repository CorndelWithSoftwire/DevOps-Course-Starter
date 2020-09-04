from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import trello_items as trello

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/')
def index():
    items = trello.get_items()
    return render_template("index.html", items=items)


@app.route('/', methods=['POST'])
def add_item():
    item_title = request.form.get('title')
    trello.add_item(item_title)
    items = trello.get_items()
    return render_template("index.html", items=items)


@app.route('/complete/<id>', methods=['POST'])
def complete_item(id):
    print('iitemid ***************** ' + id)
    trello.move_to_done(id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
