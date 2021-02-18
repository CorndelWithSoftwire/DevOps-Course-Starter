from flask import Flask, render_template, request, redirect, url_for
import trello_items as trello_items
import items_view_model as ItemsViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')

    @app.route('/')
    def index():
        trello_items.get_items()
        return redirect('tasks')

    @app.route('/tasks')
    def list_tasks():
        items = trello_items.get_items()
        # Get ToDo items
        view_model = ItemsViewModel.ItemsViewModel(items)

        return render_template('index.html', view_model=view_model)

    @app.route('/add', methods=['POST'])
    def add_item():
        task = request.form['task_description']
        trello_items.add_item(task)

        return redirect(url_for('index'))

    @app.route('/tasks/<id>/complete', methods=['POST'])
    def complete_item(id):
        trello_items.markAsDone(id)

        return redirect(url_for('index'))

    @app.route('/tasks/<id>/remove', methods=['POST'])
    def remove_item(id):
        trello_items.remove_item(id)

        return redirect(url_for('index'))

    @app.route('/tasks/<id>/inprogress', methods=['POST'])
    def inprogress_item(id):
        trello_items.inprogress_item(id)

        return redirect(url_for('index'))

    @app.route('/tasks/<id>', methods=['GET'])
    def get_item(id):
        singleitem = trello_items.get_single_item(id)
        #print(singleitem)
        return render_template("index.html", ViewModel=singleitem)

    # All the routes and setup code etc
    return app

if __name__ == '__main__':
    create_app().run()

