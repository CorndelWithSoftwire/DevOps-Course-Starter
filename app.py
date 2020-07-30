from flask import Flask, render_template, request, redirect, url_for
from session_items import get_items, add_item

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

def renderIndex():
    full_list = get_items()
    list_of_titles = []
    for item in full_list:
        list_of_titles.append(item['title'])
    return render_template('index.html', list=list_of_titles)

if __name__ == '__main__':
    app.run()
