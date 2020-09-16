from flask import Flask, render_template, redirect

from todo_app.flask_config import Config
import requests

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def new_todo():
    trello_post(request.form['add_todo'], request.form['add_desc'], request.form['due_date'])
    app.logger.info('Processing create new card request')
    return redirect('/')


if __name__ == '__main__':
    app.run()
