from flask import Flask, redirect, render_template, request, url_for
import trello_cards
import session_items as session
import os

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/', methods=['POST', 'GET'])
def get_items():
    todo = session.get_items()
    return render_template('index.html', todos=todo)


@app.route('/', methods=['POST'])
def add_item():
    name = request.form['todo.name']

    session.add_item(name)
    return render_template('index.html')



@app.route('/item/<id>', methods=['POST', 'GET'])
def get_item(id):
    if request.method == 'POST':
        item = session.get_item(id)
    return render_template('oneItemDisplay.html', item=item)


@app.route('/save', methods=['POST'])
def save_item(item):
    item = session.save_item(item)        

    return redirect("/")

@app.route('/delete/<id>', methods=['POST'])
def delete_item(id):
    item = session.get_item(id)

    session.delete_item(item)

    # return render_template('index.html')
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
