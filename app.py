from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('TRELLO_KEY'))
print(os.getenv('TRELLO_TOKEN'))

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/', methods=['get'])
def index():
    return render_template('index.html', listall=session.get_items())

@app.route('/additem', methods=['post'])
def add():
    newItem = request.form.get('new_title')
    session.add_item(newItem)
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run()