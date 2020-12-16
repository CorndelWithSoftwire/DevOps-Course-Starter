from flask import Flask, render_template, request, redirect, url_for
import Trello_items as trello
import viewmodel as vm

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')

    @app.route('/')
    def index():
        items = trello.get_items_trello()
        items=sorted(items, key=lambda k: k.status, reverse=True)
        item_view_model = vm.ViewModel(items)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/<id>/completed', methods=['POST'])
    def completeditem(id):
        trello.mark_item_done_trello(id)
        return redirect('/') 

    @app.route('/<id>/todo', methods=['POST'])
    def todoitem(id):
        trello.mark_item_todo_trello(id)
        return redirect('/') 

    @app.route('/<id>/doing', methods=['POST'])
    def doingitem(id):
        trello.mark_item_doing_trello(id)
        return redirect('/') 

    @app.route('/newitems', methods=['POST'])
    def newitems():
        itemname = request.form.get('Title')
        trello.add_item_trello(itemname)
        return redirect('/') 

    if __name__ == '__main__':
        app.run()
    return app