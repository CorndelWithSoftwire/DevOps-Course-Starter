import os

import dateutil.parser
from flask import Flask, render_template, request, redirect

from todoapp.mongo_data_access import *
from todoapp.viewmodel import ViewModel


def createListWithStatus(status, itemList):
    return [TodoItem(x['title'], status, x['_id'], duedate=x['duedate'], last_modified=x['last_modified']) for x in
            itemList]


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object('todoapp.flask_config.Config')

    MongoDatabase.DB_URL = os.getenv("DB_URL")

    board_lists = Lists(Lists.TODO_LIST_NAME, Lists.DONE_LIST_NAME)

    # Jinja filters
    @app.template_filter()
    def format_datetime(value):
        fromisoformat = dateutil.parser.parse(value)
        return fromisoformat.strftime("%b %d")

    app.jinja_env.filters['due_date_filter'] = format_datetime

    @app.route('/')
    def index():
        get_items = MongoGetCards(MongoDatabase(), board_lists.list_to_status_map)

        get_todo_list = get_items.fetchForList(board_lists.todo_list_id)
        to_do_items = createListWithStatus(NOT_STARTED, get_todo_list)

        get_done_list = get_items.fetchForList(board_lists.done_list_id)
        done_items = createListWithStatus(COMPLETED, get_done_list)

        items = to_do_items + done_items
        sorted_items = sorted(items, key=lambda item: item.status, reverse=True)

        item_view_model = ViewModel(sorted_items)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/additem', methods=['POST'])
    def add_item():
        title = request.form.get('newitem')
        duedate = request.form.get('duedate')

        MongoAddCard(MongoDatabase(), board_lists.todo_list_id).add(TodoItem(title, NOT_STARTED, duedate=duedate))

        return redirect(request.referrer)

    @app.route('/deleteitem/<id>', methods=['POST'])
    def delete_item(id):
        MongoDeleteCard(MongoDatabase(), board_lists.status_to_list_map).delete(id)

        return redirect(request.referrer)

    @app.route('/check/<id>', methods=['POST'])
    def check_item(id):
        new_list = board_lists.todo_list_id
        old_list = board_lists.done_list_id
        if request.form.get(id):
            new_list = board_lists.done_list_id
            old_list = board_lists.todo_list_id

        MongoUpdateCard(MongoDatabase()).update(id, old_list, new_list)
        return redirect(request.referrer)

    return app


if __name__ == '__main__':
    create_app().run(debug=True, host='0.0.0.0')
