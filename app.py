from flask import Flask, render_template, request, redirect, url_for
from session_items import get_items, add_item, get_item, save_item
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    return render_template('index.html', items=get_items())

@app.route('/add', methods=['POST'])
def add():
    add_item(request.form.get('input_field1'))
    return redirect(url_for('index'))

@app.route('/mark', methods=['POST'])
def mark():
    id = request.form.get('input_field2')
    item = get_item(id)
    item['status'] = 'Completed'
    save_item(item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
