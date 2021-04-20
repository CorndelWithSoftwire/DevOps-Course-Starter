from flask import Flask, render_template, request, redirect, url_for, session, make_response
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
#from flask_user import roles_required
import mongo_items as mongo_items
from requests_oauthlib import OAuth2Session
import items_view_model as ItemsViewModel
import os
import requests
from oauthlib.oauth2 import WebApplicationClient
from flask.json import jsonify
from user import User
#import login_manager as login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')
    #app.secret_key = os.getenv("SECRET_KEY")
    #app.config["SECRET_KEY"]=os.getenv("SECRET_KEY")

    login_managers = LoginManager()
    login_managers.init_app(app)

    client_id = os.getenv("GIT_CLIENT_ID")
    client_secret = os.getenv("GIT_CLIENT_SECRET")
    authorization_base_url = 'https://github.com/login/oauth/authorize'

    #login_manager.login_managers.init_app(app)


    @login_managers.unauthorized_handler
    def unauthenticated():
        client = WebApplicationClient(client_id=client_id)       
        uri = client.prepare_request_uri(authorization_base_url)

        return redirect(uri)

    @login_managers.user_loader
    def load_user(user_id):
        try:
            return User(user_id)
        except:
            return None

    @app.route('/')
    #@login_required
    def index():
        if current_user.is_authenticated:
            print("User logged in")
        else:
            print("User not logged in")

        # items = mongo_items.get_items()
        # view_model = ItemsViewModel.ItemsViewModel(items)

        # return render_template('index.html', view_model=view_model)
        return redirect('tasks')
    
    @app.route('/tasks')
    @login_required
    def list_tasks():
        items = mongo_items.get_items()
        # Get ToDo items
        view_model = ItemsViewModel.ItemsViewModel(items)

        return render_template('index.html', view_model=view_model)

    @app.route('/add', methods=['POST'])
    @login_required
    def add_item():
        task = request.form['task_description']
        mongo_items.add_item(task)

        return redirect(url_for('index'))

    @app.route('/tasks/<id>/complete', methods=['POST'])
    @login_required
    def complete_item(id):
        mongo_items.markAsDone(id)

        return redirect(url_for('index'))

    @app.route('/tasks/<id>/remove', methods=['POST'])
    @login_required
    def remove_item(id):
        mongo_items.remove_item(id)

        return redirect(url_for('index'))

    @app.route('/tasks/<id>/inprogress', methods=['POST'])
    @login_required
    def inprogress_item(id):
        mongo_items.inprogress_item(id)

        return redirect(url_for('index'))

    @app.route('/callback')
    def callback():
        get_code = request.args.get('code')
        client = WebApplicationClient(client_id=client_id) 
        url,headers,body = client.prepare_token_request('https://github.com/login/oauth/access_token', code=get_code)
        git_access_key = requests.post(url, headers=headers, data=body, auth=(client_id, client_secret))
        git_json = client.parse_request_body_response(git_access_key.text)
        git_user_request = client.add_token("https://api.github.com/user")
        git_user = requests.get(git_user_request[0], headers=git_user_request[1]).json()
        git_login = User(git_user['id'])
        login_user(git_login)

        return redirect('/')

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()  
        return redirect('/')




    return app


if __name__ == '__main__':
    create_app().run()

