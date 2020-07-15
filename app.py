from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    return render_template('index.html', items=session.get_items())

@app.route('/add', methods=['POST'])
def add():
    session.add_item(request.form.get('input_field1'))
    return redirect(url_for('index'))

@app.route('/mark', methods=['POST'])
def mark():
    id = request.form.get('input_field2')
    item = session.get_item(id)
    item['status'] = 'Completed'
    session.save_item(item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
