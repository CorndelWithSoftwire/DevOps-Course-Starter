from flask import Flask, render_template, request, redirect, url_for
import trello_items as trello_items
import ItemsViewModel as ItemsViewModel

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
        thingstodo = ItemsViewModel.ItemsViewModel(items)
        thingstodo.get_item_thingstodo()
    
        # Get Doing items
        doing = ItemsViewModel.ItemsViewModel(items)
        doing.get_item_doing()

        # Get ALL Done items
        done_all = ItemsViewModel.ItemsViewModel(items)
        done_all.show_all_done_items()

        # Get all Done items completed TODAY
        done_today = ItemsViewModel.ItemsViewModel(items)
        done_today.recent_done_items()

        #  # Get ALL Done items completed before today
        done_older = ItemsViewModel.ItemsViewModel(items)
        done_older.older_done_items()

        return render_template('index.html', thingstodo=thingstodo, doing=doing, done_all=done_all, done_older=done_older, done_today=done_today)

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
        singleitem = trello_items.get_item(id)
        print(singleitem)
        return render_template("index.html", singleitem=singleitem)

    # All the routes and setup code etc
    return app

if __name__ == '__main__':
    create_app().run()

