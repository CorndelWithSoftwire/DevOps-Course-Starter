from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    # return 'Hello World!'

    return render_template('index.html', items = session.get_items())



@app.route('/', methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        NewItem = request.form["NewItem"]
        session.add_item(NewItem)
        return render_template('index.html', items = session.get_items())
        

if __name__ == '__main__':
    app.run()
