from flask import Flask, redirect, render_template, request, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/')
def get_items():
    return render_template('index.html', todos=session.get_items())


@app.route('/item/<id>')
def get_item(id):
    item = session.get_item(id)
    return render_template('oneItemDisplay.html', item=item)

@app.route('/', methods=['POST'])
def add_item():
    session.add_item(request.form.get("title"))
    return redirect("/")


@app.route('/save', methods=['POST'])
def save_item(item):
    item = session.save_item(item)        

    return redirect("/")

@app.route('/delete/<id>', methods=['POST'])
def delete_item(id):
    item = session.get_item(id)

    session.delete_item(item)

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
