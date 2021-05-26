import os
import random
import string
from functools import wraps

import dateutil.parser
import flask
import requests
from dotenv import find_dotenv, load_dotenv
from flask import Flask, render_template, request, redirect, current_app
from flask_login import LoginManager, login_required, login_user, current_user
from oauthlib.oauth2 import WebApplicationClient

from todoapp.common import TodoItem, NOT_STARTED, Lists, COMPLETED
from todoapp.dao.mongo_role import MongoGetUsers, MongoUpdateRole, MongoAddUser, MongoGetUser, MongoDeleteUser
from todoapp.mongo_data_access import *
from todoapp.mongo_database import MongoDatabase
from todoapp.user import User
from todoapp.viewmodel import ViewModel

def authorize_for(role):
    def authorize(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if current_app.config.get('LOGIN_DISABLED') or current_user.role == role:
                return func(*args, **kwargs)
            return flask.abort(401)

        return decorated_view
    return authorize


def createListWithStatus(status, itemList):
    return [TodoItem(x['title'], status, x['_id'], duedate=x['duedate'], last_modified=x['last_modified']) for x in
            itemList]


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object('todoapp.flask_config.Config')

    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=False)

    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    # session
    app.config['SECRET_KEY'] = 'SFGBSRTHRYHDSFVSGBTYHYWG'
    app.config['SESSION_TYPE'] = 'filesystem'

    MongoDatabase.DB_URL = os.getenv("DB_URL")

    board_lists = Lists(Lists.TODO_LIST_NAME, Lists.DONE_LIST_NAME)

    # Jinja filters
    @app.template_filter()
    def format_datetime(value):
        fromisoformat = dateutil.parser.parse(value)
        return fromisoformat.strftime("%b %d")

    app.jinja_env.filters['due_date_filter'] = format_datetime

    # flask-login
    login_manager = LoginManager()
    login_manager.init_app(app)

    client = WebApplicationClient(CLIENT_ID)
    csrf_state = ''

    @login_manager.unauthorized_handler
    def unauthenticated():
        csrf_state = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        request_uri = client.prepare_request_uri('https://github.com/login/oauth/authorize', state=csrf_state)

        return redirect(request_uri)

    @app.route('/login/callback')
    def login_callback():
        # Get access token
        code = request.args.get("code")
        token_url, headers, body = client.prepare_token_request('https://github.com/login/oauth/access_token',
                                                                client_id=CLIENT_ID,
                                                                client_secret=CLIENT_SECRET,
                                                                code=code,
                                                                state=csrf_state
                                                                )

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }

        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(
                CLIENT_ID,
                CLIENT_SECRET
            ),
        )

        client.parse_request_body_response(token_response.content)

        # request for user
        uri, headers, body = client.add_token('https://api.github.com/user')

        userinfo_response = requests.get(uri, headers=headers)

        user_id = userinfo_response.json()['login']
        login_user(User(user_id))

        return redirect("/")

    @login_manager.user_loader
    def load_user(user_id):
        user = MongoGetUser(MongoDatabase()).fetch(user_id)
        return User(user["id"], user["role"]) if user is not None else User(user_id)

    @app.route('/')
    @login_required
    def index():
        get_items = MongoGetCards(MongoDatabase(), board_lists.list_to_status_map)

        get_todo_list = get_items.fetch_for_list(board_lists.todo_list_id)
        to_do_items = createListWithStatus(NOT_STARTED, get_todo_list)

        get_done_list = get_items.fetch_for_list(board_lists.done_list_id)
        done_items = createListWithStatus(COMPLETED, get_done_list)

        items = to_do_items + done_items
        sorted_items = sorted(items, key=lambda item: item.status, reverse=True)

        item_view_model = ViewModel(sorted_items)
        return render_template('index.html', view_model=item_view_model, user=current_user)

    @app.route('/additem', methods=['POST'])
    @login_required
    @authorize_for(role = 'writer')
    def add_item():
        title = request.form.get('newitem')
        duedate = request.form.get('duedate')

        MongoAddCard(MongoDatabase(), board_lists.todo_list_id).add(TodoItem(title, NOT_STARTED, duedate=duedate))

        return redirect(request.referrer)

    @app.route('/deleteitem/<id>', methods=['POST'])
    @login_required
    @authorize_for(role = 'writer')
    def delete_item(id):
        MongoDeleteCard(MongoDatabase(), board_lists.status_to_list_map).delete(id)

        return redirect(request.referrer)

    @app.route('/check/<id>', methods=['POST'])
    @login_required
    @authorize_for(role = 'writer')
    def check_item(id):
        new_list = board_lists.todo_list_id
        old_list = board_lists.done_list_id
        if request.form.get(id):
            new_list = board_lists.done_list_id
            old_list = board_lists.todo_list_id

        MongoUpdateCard(MongoDatabase()).update(id, old_list, new_list)
        return redirect(request.referrer)

    @app.route('/users', methods=['GET'])
    @login_required
    @authorize_for(role = 'admin')
    def list_users():
        users = MongoGetUsers(MongoDatabase()).fetch()
        return render_template('users.html', users=users, user=current_user)

    @app.route('/users/<id>', methods=['POST'])
    @login_required
    @authorize_for(role = 'admin')
    def update_role(id):
        role = request.form.get('role')

        MongoUpdateRole(MongoDatabase()).update(id, role)
        return redirect(request.referrer)

    @app.route('/adduser', methods=['POST'])
    @login_required
    @authorize_for(role = 'admin')
    def add_user():
        user_id = request.form.get('newuser')
        role = request.form.get('role')

        database = MongoDatabase()

        user = MongoGetUser(database).fetch(user_id)
        if user is None:
            MongoAddUser(database).add(user_id, role)
        else:
            MongoUpdateRole(database).update(user_id, role)
        return redirect(request.referrer)

    @app.route('/updateuser/<id>', methods=['POST'])
    @login_required
    @authorize_for(role = 'admin')
    def update_user(id):
        role = request.form.get('role')

        database = MongoDatabase()
        MongoUpdateRole(database).update(id, role)
        return redirect(request.referrer)

    @app.route('/deleteuser/<id>', methods=['POST'])
    @login_required
    @authorize_for(role = 'admin')
    def delete_user(id):
        database = MongoDatabase()
        MongoDeleteUser(database).delete(id)
        return redirect(request.referrer)

    return app


if __name__ == '__main__':
    create_app().run(debug=True, host='0.0.0.0')
