from flask import Flask, render_template, request, redirect, url_for
from operator import itemgetter
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')
global sortSwitch
sortSwitch = True


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        session.add_item(request.form['item_title'])

    items = session.get_items()
    global sortSwitch
    if sortSwitch:
        items = sorted(items, key=itemgetter('status'))
    else:
        items = sorted(items, key=itemgetter('status'), reverse=True)
    return render_template('index.html', items=items)


@app.route('/item/<id>', methods=['POST', 'GET'])
def get_item(id):
    if request.method == 'POST':
        item = session.get_item(id)
        item = session.create_new_item(item['id'], item['title'], 'Complete')

        session.save_item(item)
    return render_template('todoSingle.html', items=session.get_item(id))


@app.route('/delete_item/<id>', methods=['POST'])
def delete_item(id):
    if request.method == 'POST':
        item = session.get_item(id)

        session.delete_item(item)
    return redirect("/")


@app.route('/sorted_items')
def sort_item():
    global sortSwitch
    if sortSwitch:
        sortSwitch = False
    else:
        sortSwitch = True
    return redirect("/")


if __name__ == '__main__':
    app.run()
