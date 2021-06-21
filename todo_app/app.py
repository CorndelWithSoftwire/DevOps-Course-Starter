from flask import Flask, render_template, request, redirect, url_for
import Mongo_items as mongo
import viewmodel as vm

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')

    @app.route('/')
    def index():
        items = mongo.get_items_mongo()
        items=sorted(items, key=lambda k: k.status, reverse=True)
        item_view_model = vm.ViewModel(items)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/<id>/doingcompleted', methods=['POST'])
    def doingcompleteditem(id):
        mongo.mark_doing_item_done_mongo(id)
        return redirect('/') 

    @app.route('/<id>/todocompleted', methods=['POST'])
    def todocompleteditem(id):
        mongo.mark_todo_item_done_mongo(id)
        return redirect('/') 

    @app.route('/<id>/doingtodo', methods=['POST'])
    def doingtodoitem(id):
        mongo.mark_doing_item_todo_mongo(id)
        return redirect('/') 

    @app.route('/<id>/donetodo', methods=['POST'])
    def donetodoitem(id):
        mongo.mark_done_item_todo_mongo(id)
        return redirect('/') 

    @app.route('/<id>/tododoing', methods=['POST'])
    def tododoingitem(id):
        mongo.mark_todo_item_doing_mongo(id)
        return redirect('/') 

    @app.route('/<id>/donedoing', methods=['POST'])
    def donedoingitem(id):
        mongo.mark_done_item_doing_mongo(id)
        return redirect('/') 

    @app.route('/newitems', methods=['POST'])
    def newitems():
        itemname = request.form.get('Title')
        mongo.add_item_mongo(itemname)
        return redirect('/') 

    if __name__ == '__main__':
        app.run()
    return app