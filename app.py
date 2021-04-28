from flask import Flask, render_template, request, redirect, url_for, session, make_response, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
import mongo_items as mongo_items
from requests_oauthlib import OAuth2Session
import items_view_model as ItemsViewModel
import os
import requests
from oauthlib.oauth2 import WebApplicationClient
from user import User

def create_app():
    app = Flask(__name__)
    Flask.make_null_session
    app.config.from_object('flask_config.Config')
    app.config['LOGIN_DISABLED'] = os.environ.get('LOGIN_DISABLED', 'False').lower() in ('true', 't', '1')

    login_managers = LoginManager()

    client_id = os.getenv("GIT_CLIENT_ID")
    client_secret = os.getenv("GIT_CLIENT_SECRET")
    authorization_base_url = 'https://github.com/login/oauth/authorize'

    @login_managers.unauthorized_handler
    def unauthenticated():
        client = WebApplicationClient(client_id=client_id)       
        uri = client.prepare_request_uri(authorization_base_url)

        return redirect(uri)

    @login_managers.user_loader
    def load_user(user_id):
        
        return User(user_id)


    @app.route('/')
    def index():
        if current_user.is_authenticated is False:
            flash('You must be logged in to manage tasks','alert alert-danger')

        items = mongo_items.get_items()
        # Get ToDo items
        view_model = ItemsViewModel.ItemsViewModel(items)

        return render_template('index.html', view_model=view_model)
        
    
    @app.route('/tasks')
    def list_tasks():

        return redirect(url_for('index'))

    @app.route('/add', methods=['POST'])
    @login_required
    def add_item():
        task = request.form['task_description']
        #if(current_user.userrole == 'writer'):
        mongo_items.add_item(task)
        #else:
        #    flash('You must be logged in to add tasks','alert alert-danger')
        return redirect(url_for('index'))

    @app.route('/tasks/<id>/complete', methods=['POST'])
    @login_required
    def complete_item(id):
        if(current_user.userrole == 'writer'):
            mongo_items.markAsDone(id)
        else:
            flash('You must be logged in to Complete tasks','alert alert-danger')

        return redirect(url_for('index'))

    @app.route('/tasks/<id>/remove', methods=['POST'])
    @login_required
    def remove_item(id):
        if(current_user.userrole == 'writer'):
            mongo_items.remove_item(id)
        else:
            flash('You must be logged in to Remove tasks','alert alert-danger')

        return redirect(url_for('index'))

    @app.route('/tasks/<id>/inprogress', methods=['POST'])
    @login_required
    def inprogress_item(id):
        if(current_user.userrole == 'writer'):
            mongo_items.inprogress_item(id)
        else:
            flash('<strong>Success!</strong>You must be logged in to InProgress tasks','alert alert-danger')

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
        git_login = User(git_user['login'])
        login_user(git_login)

        return redirect('/')

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()  
        flash('You have been logged out','alert alert-success')
        session.clear()
        return redirect('/')


    login_managers.init_app(app)

    if __name__ == '__main__':
        app.run()

    return app