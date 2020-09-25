from trello_request import *

from flask import Flask, render_template, request, redirect
import dateutil.parser

from viewmodel import ViewModel

def createListWithStatus(status, itemList):
    return [TodoItem(x['name'], status, x['id'], duedate=x['due'], last_modified=x['dateLastActivity']) for x in
            itemList]


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object('flask_config.Config')

    todo_list_id = os.getenv("TODO_LIST_ID")
    done_list_id = os.getenv("DONE_LIST_ID")

    board_lists = Lists(todo_list_id, done_list_id)

    # Jinja filters
    @app.template_filter()
    def format_datetime(value):
        fromisoformat = dateutil.parser.parse(value)
        return fromisoformat.strftime("%b %d")

    app.jinja_env.filters['due_date_filter'] = format_datetime

    @app.route('/')
    def index():
        trello_get_cards = TrelloGetCards(board_lists.list_to_status_map)

        getTodoList = trello_get_cards.fetchForList(board_lists.todo_list_id)
        toDoItems = createListWithStatus(NOT_STARTED, getTodoList)

        getDoneList = trello_get_cards.fetchForList(board_lists.done_list_id)
        doneItems = createListWithStatus(COMPLETED, getDoneList)

        items = toDoItems + doneItems
        sorteditems = sorted(items, key=lambda item: item.status, reverse=True)

        item_view_model = ViewModel(sorteditems)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/additem', methods=['POST'])
    def additem():
        title = request.form.get('newitem')
        duedate = request.form.get('duedate')

        TrelloAddCard(board_lists.todo_list_id).add(TodoItem(title, NOT_STARTED, duedate=duedate))

        return redirect(request.referrer)

    @app.route('/deleteitem/<id>', methods=['POST'])
    def deleteitem(id):
        TrelloDeleteCard().delete(id)

        return redirect(request.referrer)

    @app.route('/check/<id>', methods=['POST'])
    def checkitem(id):
        item = TrelloGetCards(board_lists.list_to_status_map).fetchCard(id)
        list = board_lists.todo_list_id
        if request.form.get(id):
            list = board_lists.done_list_id

        TrelloUpdateCard().update(item, list)
        return redirect(request.referrer)

    return app


if __name__ == '__main__':
    create_app().run()
