from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/')
def index():
    items = session.get_items()
    return render_template('index.html', items=items)


@app.route('/items', methods=['POST'])
def add_item():
    title = request.form['text-input']
    session.add_item(title)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
