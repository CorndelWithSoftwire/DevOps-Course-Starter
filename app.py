from trello_request import *

from flask import Flask, render_template, request, redirect
import dateutil.parser

from viewmodel import ViewModel

app = Flask(__name__, static_url_path='/static')
app.config.from_object('flask_config.Config')


# Jinja filters
@app.template_filter()
def format_datetime(value):
    fromisoformat = dateutil.parser.parse(value)
    return fromisoformat.strftime("%b %d")


app.jinja_env.filters['due_date_filter'] = format_datetime


@app.route('/')
def index():
    getTodoList = TrelloGetCards().fetchForList(TODO_LIST_ID)
    toDoItems = [TodoItem(x['name'], NOT_STARTED, x['id'], duedate=x['due']) for x in getTodoList]

    getDoneList = TrelloGetCards().fetchForList(DONE_LIST_ID)
    doneItems = [TodoItem(x['name'], COMPLETED, x['id'], duedate=x['due']) for x in getDoneList]

    items = toDoItems + doneItems
    sorteditems = sorted(items, key=lambda item: item.status, reverse=True)

    item_view_model = ViewModel(sorteditems)
    return render_template('index.html', view_model=item_view_model)


@app.route('/additem', methods=['POST'])
def additem():
    title = request.form.get('newitem')
    duedate = request.form.get('duedate')

    TrelloAddCard(TODO_LIST_ID).add(TodoItem(title, NOT_STARTED, duedate=duedate))

    return redirect(request.referrer)


@app.route('/deleteitem/<id>', methods=['POST'])
def deleteitem(id):
    TrelloDeleteCard().delete(id)

    return redirect(request.referrer)


@app.route('/check/<id>', methods=['POST'])
def checkitem(id):
    item = TrelloGetCards().fetchCard(id)
    list = TODO_LIST_ID
    if request.form.get(id):
        list = DONE_LIST_ID

    TrelloUpdateCard().update(item, list)
    return redirect(request.referrer)


if __name__ == '__main__':
    app.run()
