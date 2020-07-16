from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__, template_folder="./templates")
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    all_items = session.get_items()
    all_items = sorted(all_items, key=lambda i: i['status'], reverse=True)

    return render_template('index.html', items=all_items)

@app.route('/add', methods=['POST'])
def add_item():
    title = request.form['title']
    session.add_item(title)
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete_item(id):
    item = session.get_item(id)
    if item == None:
        return redirect(url_for('index'))

    item['status'] = 'Completed'
    session.save_item(item)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
