from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user
import mongo_items as mongo_items
import items_view_model as ItemsViewModel
import os
from oauthlib.oauth2 import WebApplicationClient

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')

    login_manager = LoginManager()

    client_id = os.getenv("GIT_CLIENT_ID")
    client_secret = os.getenv("GIT_CLIENT_SECRET")
    authorization_base_url = 'https://github.com/login/oauth/authorize'

    @login_manager.unauthorized_handler
    def unauthenticated():
        client = WebApplicationClient(client_id)       
        uri = client.prepare_request_uri(authorization_base_url)

        return redirect(uri)
        #pass

    @login_manager.user_loader
    def load_user(user_id):
        return None
    

    @login_required
    @app.route('/')
    def index():
        mongo_items.get_items()
        return redirect('tasks')
    
    @login_required
    @app.route('/tasks')
    def list_tasks():
        items = mongo_items.get_items()
        # Get ToDo items
        view_model = ItemsViewModel.ItemsViewModel(items)

        return render_template('index.html', view_model=view_model)

    @login_required
    @app.route('/add', methods=['POST'])
    def add_item():
        task = request.form['task_description']
        mongo_items.add_item(task)

        return redirect(url_for('index'))

    @login_required
    @app.route('/tasks/<id>/complete', methods=['POST'])
    def complete_item(id):
        mongo_items.markAsDone(id)

        return redirect(url_for('index'))

    @login_required
    @app.route('/tasks/<id>/remove', methods=['POST'])
    def remove_item(id):
        mongo_items.remove_item(id)

        return redirect(url_for('index'))

    @login_required
    @app.route('/tasks/<id>/inprogress', methods=['POST'])
    def inprogress_item(id):
        mongo_items.inprogress_item(id)

        return redirect(url_for('index'))

    # All the routes and setup code etc

    login_manager.init_app(app)

    return app


if __name__ == '__main__':
    create_app().run()

