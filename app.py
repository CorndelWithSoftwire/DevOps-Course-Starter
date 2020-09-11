from flask import Flask, redirect, render_template, request, url_for
import trello_cards
import session_items as session
import os

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/', methods=['GET'])
def get_items():
    todo = session.get_items()

    return render_template('index.html', todos=todo)


@app.route('/', methods=['POST'])
def add_item():
    name = request.form['name']
    desc = request.form['desc']

    session.add_new_item(name, desc)
    return redirect('/')

@app.route('/done', methods=['GET'])
def get_done_items():
    done = session.get_done_items()

    return render_template('done.html', dones=done)

@app.route('/done', methods=['POST'])
def update_item():
    id = request.form['item_id']
    session.update_item(id)

    return redirect('/done')


@app.route('/delete_item', methods=['POST'])
def delete_item(id):
    id = request.form['item_id']
    session.delete_item()

    # return render_template('index.html')
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
