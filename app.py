from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    items = session.get_items()
    return render_template('index.html', items=items)
    #return 'Hello World!'

@app.route('/add', methods=['POST'])
def addToDo():
    title = request.form['title']
    session.add_item(title)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
