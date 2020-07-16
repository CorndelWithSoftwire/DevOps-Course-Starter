from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/items')
def index():
    items = session.get_items()
    return render_template('index.html', items=items)

@app.route('/items', methods=['POST'])
def add_item():
    title = request.form['title']
    item = session.add_item(title)
    items = session.get_items()

    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run()
