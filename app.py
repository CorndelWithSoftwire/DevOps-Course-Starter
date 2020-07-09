from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        session.add_item(request.form.get('item'))
    else:
        pass
    
    return render_template('index.html', data=session.get_items())


if __name__ == '__main__':
    app.run()
