from flask import Flask, render_template, request, redirect, url_for
import todo_app.trello_items as trello
from todo_app.viewmodel import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object('todo_app.flask_config.Config')

    @app.route('/')
    def index():
        items = trello.get_items()
        item_view_model = ViewModel(items)
        return render_template("index.html", view_model=item_view_model)

    @app.route('/', methods=['POST'])
    def add_item():
        item_title = request.form.get('title')
        item_desc = request.form.get('desc')
        trello.add_item(item_title, item_desc)
        return redirect(url_for('index'))

    @app.route('/complete/<id>', methods=['POST'])
    def complete_item(id):
        trello.move_to_done(id)
        return redirect(url_for('index'))

    if __name__ == '__main__':
        app.run()

    return app
