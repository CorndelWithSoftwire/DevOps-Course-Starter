from flask import Flask, render_template, request, redirect, url_for
# import session_items as session
import ApiAccess as api


app = Flask(__name__)
app.config.from_object('flask_config.Config')

obj1 = api.AccessTrelloApi()


def get_items():

    Items1 = obj1.getCardsFromTrelloList(
        api.TODOLISTURL, 'To Do')

    Items2 = obj1.getCardsFromTrelloList(
        api.DONELISTURL, 'Done')

    return Items1 + Items2


@app.route('/')
def index():
    return render_template('index.html', items=get_items())


@app.route('/add_item/', methods=['POST'])
def add_item():
    NewItem = request.form["NewItem"]
    #obj1 = api.AccessTrelloApi()
    obj1.AddItemTodoList(NewItem)
    return render_template('index.html', items=get_items())


@app.route('/complete_item/<item>', methods=['GET'])
def complete_item(item):
    #obj1 = api.AccessTrelloApi()
    obj1.MarkItemAsDone(item)
    return render_template('index.html', items=get_items())


"""
@app.route('/', methods=['POST'])
def AddListItem():
    # if request.method == 'POST':
    NewItem = request.form["NewItem"]
    # session.add_item(NewItem)
    obj1 = api.AccessTrelloApi()
    obj1.AddItemTodoList(NewItem)
    return render_template('index.html', items=session.get_items())
"""


if __name__ == '__main__':
    app.run(debug=True)

    # if request.method == 'POST':
    #    NewItem = request.form["NewItem"]
    #    obj1 = api.AccessTrelloApi()
    #    obj1.AddItemTodoList(NewItem)
    #    return render_template('index.html', items=session.get_items())
    # else:
