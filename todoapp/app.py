import os

import dateutil.parser
from flask import Flask, render_template, request, redirect

from todoapp.trello_request import *
from todoapp.viewmodel import ViewModel


def createListWithStatus(status, itemList):
    return [TodoItem(x['name'], status, x['id'], duedate=x['due'], last_modified=x['dateLastActivity']) for x in
            itemList]


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object('todoapp.flask_config.Config')

    TrelloRequest.APP_API_KEY = os.getenv("APP_API_KEY")
    TrelloRequest.APP_TOKEN = os.getenv("APP_TOKEN")

    board_lists = setup_lists()

    # Jinja filters
    @app.template_filter()
    def format_datetime(value):
        fromisoformat = dateutil.parser.parse(value)
        return fromisoformat.strftime("%b %d")

    app.jinja_env.filters['due_date_filter'] = format_datetime

    @app.route('/')
    def index():
        trello_get_cards = TrelloGetCards(board_lists.list_to_status_map)

        get_todo_list = trello_get_cards.fetchForList(board_lists.todo_list_id)
        to_do_items = createListWithStatus(NOT_STARTED, get_todo_list)

        get_done_list = trello_get_cards.fetchForList(board_lists.done_list_id)
        done_items = createListWithStatus(COMPLETED, get_done_list)

        items = to_do_items + done_items
        sorted_items = sorted(items, key=lambda item: item.status, reverse=True)

        item_view_model = ViewModel(sorted_items)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/additem', methods=['POST'])
    def add_item():
        title = request.form.get('newitem')
        duedate = request.form.get('duedate')

        TrelloAddCard(board_lists.todo_list_id).add(TodoItem(title, NOT_STARTED, duedate=duedate))

        return redirect(request.referrer)

    @app.route('/deleteitem/<id>', methods=['POST'])
    def delete_item(id):
        TrelloDeleteCard().delete(id)

        return redirect(request.referrer)

    @app.route('/check/<id>', methods=['POST'])
    def check_item(id):
        item = TrelloGetCards(board_lists.list_to_status_map).fetchCard(id)
        list = board_lists.todo_list_id
        if request.form.get(id):
            list = board_lists.done_list_id

        TrelloUpdateCard().update(item, list)
        return redirect(request.referrer)

    return app


def setup_lists():
    board_id = os.environ['TODO_BOARD_ID']
    todo_lists_by_name, todo_lists_by_id = TrelloBoard().fetchLists(board_id)
    todo_list_id = todo_lists_by_name[Lists.TODO_LIST_NAME]
    done_list_id = todo_lists_by_name[Lists.DONE_LIST_NAME]
    return Lists(todo_list_id, done_list_id)


if __name__ == '__main__':
    create_app().run(debug=True, host='0.0.0.0')
