from flask import Flask, render_template, request, redirect
from app.trello_client import TrelloClient
from app.viewmodel import ViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.flask_config.Config')
    client = TrelloClient()

    @app.route('/', methods=['GET'])
    def index():
        sorted_items = sorted(client.get_items(), key=lambda item: item.status, reverse=True)
        view_model = ViewModel(sorted_items)
        return render_template('index.html', view_model=view_model)


    @app.route('/', methods=['POST'])
    def post_item():
        client.add_item(request.form.get('item'))
        return redirect('/')


    @app.route('/update/<id>', methods=['POST'])
    def mark_complete(id):
        client.mark_complete(id)

        return redirect('/')


    @app.route('/delete/<id>', methods=['GET'])
    def delete_item(id):
        client.delete_item_by_id(id)
        return redirect('/')    

    return app
