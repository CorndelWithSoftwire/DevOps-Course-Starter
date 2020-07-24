from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    return render_template('index.html', todos=session.get_items())



@app.route('/item/<id>')
def get_item(id):

    item = session.get_item(id)
    return render_template('OneItemDisplay.html', item=item)

@app.route('/add', methods=['POST'])
def add_item():

    if request.method == "POST":
        session.add_item(request.form.get("title"))
    return redirect("/")


@app.route('/save', methods=['POST'])
def save_item(item):

    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item

@app.route('/delete<id>', methods=['POST'])
def delete_item(item):

    if request.method == "POST":
        item = session.get_item(id)

        session.delete(item)

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
