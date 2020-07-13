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


@app.route('/update/<int:id>', methods=['POST'])
def mark_complete(id):
    item = session.get_item(id)
    item['status'] = 'Completed'

    session.save_item(item)

    return redirect('/')


if __name__ == '__main__':
    app.run()
