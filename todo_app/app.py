from flask import Flask, render_template, request, redirect, url_for
import todo_app.trello_items as trello
from todo_app.mongo_repository import MongoRepository
from todo_app.viewmodel import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object('todo_app.flask_config.Config')
    mongo_repo = MongoRepository()

    @app.route('/')
    def index():
        items = mongo_repo.get_items()
        item_view_model = ViewModel(items)
        return render_template("index.html", view_model=item_view_model)

    @app.route('/', methods=['POST'])
    def add_item():
        item_title = request.form.get('title')
        item_desc = request.form.get('desc')
        mongo_repo.add_item(item_title, item_desc)
        return redirect(url_for('index'))

    @app.route('/complete/<id>', methods=['POST'])
    def complete_item(id):
        mongo_repo.move_to_done(id)
        return redirect(url_for('index'))

    if __name__ == '__main__':
        app.run()

    return app
