from flask import Flask, render_template, request, redirect, url_for, abort
from flask_login import LoginManager, login_required
import flask_login
from flask_login.mixins import UserMixin
from oauthlib.oauth2 import WebApplicationClient
import Mongo_items as mongo
import viewmodel as vm
import os, requests, json
from functools import wraps

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')

    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        client = WebApplicationClient(os.getenv("CLIENT_ID"))
        client.state = client.state_generator()
        authredirect = client.prepare_request_uri("https://github.com/login/oauth/authorize", state=client.state)
        return redirect(authredirect)

    @login_manager.user_loader
    def load_user(user_id):
        user = User(user_id)
        return user

    login_manager.init_app(app)

    class User(UserMixin):
        def __init__(self, userid):
            self.id = userid
            if self.id == "69510597" :
                self.role = 'writer'
            else :
                self.role = 'reader'

    def writer_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if get_user_role() == 'reader':
                abort(403)
            else:
                return f(*args, **kwargs)
        return decorated_function

    def get_user_role():
        if app.config['LOGIN_DISABLED']:
            return "writer"
        else:
            return flask_login.current_user.role

    @app.route('/')
    @login_required
    def index():
        items = mongo.get_items_mongo()
        items=sorted(items, key=lambda k: k.status, reverse=True)
        item_view_model = vm.ViewModel(items)
        role = get_user_role()
        return render_template('index.html', view_model=item_view_model, role=role)

    @app.route('/login/callback')
    def callback():
        client = WebApplicationClient(os.getenv("CLIENT_ID"))
        client.state = request.args.get('state')
        code = request.args.get('code')
        tokenurl, headers, body = client.prepare_token_request('https://github.com/login/oauth/access_token', state=client.state, code=code)
        secret=os.getenv('OAUTH_SECRET')
        clientid=os.getenv("CLIENT_ID")
        tokenresponse = requests.post(tokenurl, data=body, auth=(clientid, secret))
        client.parse_request_body_response(tokenresponse.text)
        userinfo_endpoint = "https://api.github.com/user"
        uri, headers, body = client.add_token(userinfo_endpoint)
        userinfo_response = requests.get(uri, headers=headers, data=body)
        userinfo_json = userinfo_response.json()
        id = userinfo_json['id']
        flask_login.login_user(load_user(id))
        return redirect("/")

    @app.route('/<id>/doingcompleted', methods=['POST'])
    @login_required
    @writer_required
    def doingcompleteditem(id):
        mongo.mark_doing_item_done_mongo(id)
        return redirect('/') 

    @app.route('/<id>/todocompleted', methods=['POST'])
    @login_required
    @writer_required
    def todocompleteditem(id):
        mongo.mark_todo_item_done_mongo(id)
        return redirect('/') 

    @app.route('/<id>/doingtodo', methods=['POST'])
    @login_required
    @writer_required
    def doingtodoitem(id):
        mongo.mark_doing_item_todo_mongo(id)
        return redirect('/') 

    @app.route('/<id>/donetodo', methods=['POST'])
    @login_required
    @writer_required
    def donetodoitem(id):
        mongo.mark_done_item_todo_mongo(id)
        return redirect('/') 

    @app.route('/<id>/tododoing', methods=['POST'])
    @login_required
    @writer_required
    def tododoingitem(id):
        mongo.mark_todo_item_doing_mongo(id)
        return redirect('/') 

    @app.route('/<id>/donedoing', methods=['POST'])
    @login_required
    @writer_required
    def donedoingitem(id):
        mongo.mark_done_item_doing_mongo(id)
        return redirect('/') 

    @app.route('/newitems', methods=['POST'])
    @login_required
    @writer_required
    def newitems():
        itemname = request.form.get('Title')
        mongo.add_item_mongo(itemname)
        return redirect('/') 

    if __name__ == '__main__':
        app.run()
    return app