from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('web/favicon.ico')


@app.route('/items')
def index():
    items = session.get_items()
    items.sort(key=get_status)
    return render_template('index.html', items=items)


@app.route('/items', methods=['POST'])
def add_item():
    title = request.form['title']
    items = session.get_items()

    if title == '':
        return render_template('index.html', items=items)

    for item in items:
        if item['title'] == title:
            print('An item with the title ' + title + ' already exists.')
            return render_template('index.html', items=items)

    session.add_item(title)
    return render_template('index.html', items=items)


@app.route('/items/<id>')
def get_item(id):
    session.get_item(id)
    return index()


@app.route('/items/<id>', methods=['POST'])
def mark_as_completed(id):
    print('index to complete: ' + str(id))
    item = session.get_item(id)
    print('item found: ' + str(item))
    item['status'] = "Completed"
    session.save_item(item)
    return redirect(url_for('index'))


@app.route('/items/<id>/delete', methods=['POST'])
@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    session.delete_item(id)
    return redirect(url_for('index'))


@app.route('/items', methods=['DELETE'])
@app.route('/items/delete', methods=['POST'])
def delete_all_items():
    session.delete_all()
    return redirect(url_for('index'))


def get_status(item):
    return item.get('status')


if __name__ == '__main__':
    app.run()
