from flask import Flask, render_template, request, redirect, url_for
from session_items import get_items, get_item, add_item, save_item

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    return renderIndex()

@app.route('/listitem', methods=['POST'])
def addListItem():
    print("Adding Item!")
    print('Title=' + request.form.get('textbox'))
    add_item(request.form.get('textbox'))
    return renderIndex()

@app.route('/completeditem', methods=['POST'])
def updateListItem():
    print("Updating Item!")
    print(request.form.get('id'))
    item_to_update = get_item(request.form.get('id'))
    print(item_to_update)
    item_to_update['status'] = 'Done!'
    save_item(item_to_update)
    return renderIndex()

def renderIndex():
    full_list = get_items()
    return render_template('index.html', list=full_list)

if __name__ == '__main__':
    app.run()
