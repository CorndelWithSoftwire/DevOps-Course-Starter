from flask import Flask, render_template, request
from todo_app.flask_config import Config
import todo_app.data.session_items as fl

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html', items = fl.get_items())

@app.route('/add', methods=['POST'])
def add():
    fl.add_item(request.form.get('title'))
    print (request.form)
    return render_template('index.html', items = fl.get_items())

@app.route('/setstatus/<id>/<status>', methods=['POST'])
def setstatus(id,status):
    item = fl.get_item(id)
    item['status'] = status
    fl.save_item(item)
    return render_template('index.html', items = fl.get_items())

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    item = fl.get_item(id)
    fl.delete_item(item)
    return render_template('index.html', items = fl.get_items())

if __name__ == '__main__':
    app.run()
