from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/')
def index():
    return render_template('index.html', items=session.get_items())


@app.route('/item/<id>')
def get_item(id):
    return render_template('todoSingle.html', items=session.get_item(id))


@app.route('/add_item', methods=['POST'])
def create_item():
    session.add_item(request.form['user_name'])
    return render_template('index.html', items=session.get_items())


if __name__ == '__main__':
    app.run()
