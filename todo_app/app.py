import os
import requests
from flask import Flask, render_template, request, session, redirect, url_for
import todo_app.view_model as view_model
from todo_app.Task import Task
import todo_app.trello as trello

app = Flask(__name__)
headers = {
   "Accept": "application/json"
}

def create_app():
    app = Flask(__name__)
    app.config.from_object('app_config.Config')

    @app.route('/', methods=['Get'])
    def index():
        tasks = trello.get_all_tasks()        
        task_view_model = view_model.ViewModel(tasks)
        return render_template('index.html', view_model=task_view_model)

    @app.route('/add_todo', methods=['Post'])
    def add_todo_task():
        trello.create_todo_task(request.form.get('title'))
        return redirect('/')

    @app.route('/move_to_doing/<todo_task_id>', methods=['Post'])
    def move_to_doing(todo_task_id):
        trello.move_to_doing(todo_task_id)
        return redirect('/')

    @app.route('/move_to_done/<task_id>', methods=['Post'])
    def move_to_done(task_id):
        trello.move_to_done(task_id)
        return redirect('/')

    @app.route('/delete_task/<task_id>', methods=['Post'])
    def delete_task(task_id):
        trello.delete_task(task_id)
        return redirect('/')

    if __name__ == '__main__':
        app.run()
    
    return app



