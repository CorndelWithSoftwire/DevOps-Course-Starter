from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/', methods=['GET'])
def index():
    sorted_items = sorted(session.get_items(), key=lambda item: item.status, reverse=True)
    return render_template('index.html', data=sorted_items)


@app.route('/', methods=['POST'])
def post_item():
    session.add_item(request.form.get('item'))
    return redirect('/')

@app.route('/update/<id>', methods=['POST'])
def mark_complete(id):
    session.mark_complete(id)

    return redirect('/')


@app.route('/delete/<id>', methods=['GET'])
def delete_item(id):
    session.delete_item_by_id(id)
    return redirect('/')    


if __name__ == '__main__':
    app.run()
