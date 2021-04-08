from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user
import mongo_items as mongo_items
import items_view_model as ItemsViewModel
import os
from oauthlib.oauth2 import WebApplicationClient

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')

    login_managers = LoginManager()

    client_id = os.getenv("GIT_CLIENT_ID")
    client_secret = os.getenv("GIT_CLIENT_SECRET")
    authorization_base_url = 'https://github.com/login/oauth/authorize'

    @login_managers.unauthorized_handler
    def unauthenticated():
        client = WebApplicationClient(client_id)       
        uri = client.prepare_request_uri(authorization_base_url)

        return redirect(uri)
        #pass

    @login_managers.user_loader
    def load_user(user_id):
        return None
    

    
    @app.route('/')
    @login_required
    def index():
        mongo_items.get_items()
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
        ###
        return redirect('tasks')


    login_managers.init_app(app)

    return app


if __name__ == '__main__':
    create_app().run()

