from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/', methods=['get'])
def index():
    return render_template('index.html', listall=session.get_items())

@app.route('/', methods=['post'])
def add():
    newItem = request.form.get('new_title')
    session.add_item(newItem)

    return render_template('index.html', listall=session.get_items())


if __name__ == '__main__':
    app.run()
