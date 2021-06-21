from flask import Flask, render_template, request, redirect, url_for, abort
from flask_login import LoginManager, login_required
import flask_login
from flask_login.mixins import UserMixin
from oauthlib.oauth2 import WebApplicationClient
from oauthlib.oauth2.rfc6749.grant_types import client_credentials
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
        authredirect = client.prepare_request_uri("https://github.com/login/oauth/authorize", state="saxasdfaa")
        return redirect(authredirect)

    @login_manager.user_loader
    def load_user(user_id):
        user = User(user_id)
        return user

    login_manager.init_app(app)

    class User(UserMixin):
        def __init__(self, userid):
            self.user_id = userid
            self.id = userid
            if self.id == "69510597" :
                self.role = 'reader'
            else :
                self.role = 'writer'

    def checkrole(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):

            user = load_user(flask_login.current_user.id)
            if user.role == 'reader':
                abort(403)
            else:
                return f(*args, **kwargs)
        return decorated_function

    @app.route('/')
    @login_required
    def index():
        items = mongo.get_items_mongo()
        items=sorted(items, key=lambda k: k.status, reverse=True)
        item_view_model = vm.ViewModel(items)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/login/callback')
    def callback():
        code = request.args.get('code')
        client = WebApplicationClient(os.getenv("CLIENT_ID"))
        tokenurl, headers, body = client.prepare_token_request('https://github.com/login/oauth/access_token', authorization_response=request.url, state="saxasdfaa", code=code)
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
        return redirect(url_for("index"))

    @app.route('/<id>/doingcompleted', methods=['POST'])
    @login_required
    @checkrole
    def doingcompleteditem(id):
        mongo.mark_doing_item_done_mongo(id)
        return redirect('/') 

    @app.route('/<id>/todocompleted', methods=['POST'])
    @login_required
    @checkrole
    def todocompleteditem(id):
        mongo.mark_todo_item_done_mongo(id)
        return redirect('/') 

    @app.route('/<id>/doingtodo', methods=['POST'])
    @login_required
    @checkrole
    def doingtodoitem(id):
        mongo.mark_doing_item_todo_mongo(id)
        return redirect('/') 

    @app.route('/<id>/donetodo', methods=['POST'])
    @login_required
    @checkrole
    def donetodoitem(id):
        mongo.mark_done_item_todo_mongo(id)
        return redirect('/') 

    @app.route('/<id>/tododoing', methods=['POST'])
    @login_required
    @checkrole
    def tododoingitem(id):
        mongo.mark_todo_item_doing_mongo(id)
        return redirect('/') 

    @app.route('/<id>/donedoing', methods=['POST'])
    @login_required
    @checkrole
    def donedoingitem(id):
        mongo.mark_done_item_doing_mongo(id)
        return redirect('/') 

    @app.route('/newitems', methods=['POST'])
    @login_required
    @checkrole
    def newitems():
        itemname = request.form.get('Title')
        mongo.add_item_mongo(itemname)
        return redirect('/') 

    if __name__ == '__main__':
        app.run()
    return app