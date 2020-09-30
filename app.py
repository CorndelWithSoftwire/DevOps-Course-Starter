from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import ApiAccess as api


app = Flask(__name__)
app.config.from_object('flask_config.Config')

obj1 = api.AccessTrelloApi()


@app.route('/')
def index():
    return render_template('index.html', items=session.get_items())


@app.route('/', methods=['POST', 'PUT'])
def updateLists():
    if request.method == 'POST':
        NewItem = request.form["NewItem"]
        # session.add_item(NewItem)
        obj1 = api.AccessTrelloApi()
        obj1.AddItemTodoList(NewItem)
        return render_template('index.html', items=session.get_items())


if __name__ == '__main__':
    app.run(debug=True)
