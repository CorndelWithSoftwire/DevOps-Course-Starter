from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__, static_url_path='/static')
app.config.from_object('flask_config.Config')


@app.route('/')
def index():
    items = session.get_items()
    sorteditems = sorted(items, key=lambda item: item['status'], reverse=True)
    return render_template('/index.html', items = sorteditems)


@app.route('/additem', methods=['POST'])
def additem():
    todoItemTitle = request.form.get('newitem')
    session.add_item(todoItemTitle)
    return index()


@app.route('/deleteitem/<id>', methods=['POST'])
def deleteitem(id):
    session.delete_item(id)
    return index()


# TODO
@app.route('/check/<id>', methods=['POST'])
def checkitem(id):
    # todoItemTitle = request.form.get('')
    # session.add_item(todoItemTitle)
    item = session.get_item(id)
    item['status'] = 'Completed'
    session.save_item(item)
    return index()


if __name__ == '__main__':
    app.run()
