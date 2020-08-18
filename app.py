from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    #populate variable with the list of saved todo items
    items = session.get_items()
    #pass the list into the index template for display
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run()
