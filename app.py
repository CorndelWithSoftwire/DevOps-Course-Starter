from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    item_list = session.get_items()
    return render_template("index.html", items=item_list)

@app.route('/newItem', methods=['POST'])
def submitNewItem():
    session.add_item(request.form.get('itemName'))
    item_list = session.get_items()
    return render_template("index.html", items=item_list)

if __name__ == '__main__':
    app.run()
