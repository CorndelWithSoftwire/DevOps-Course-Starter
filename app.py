from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/')
def index():
    return render_template('index.html', items=session.get_items())

@app.route('/addit', methods=['GET', 'POST'])
def addit():
    if request.method == 'GET':
        return 'Meant for POST requires item'
    if request.method == 'POST':
        session.add_item(request.form.get('new_item'))
        return redirect('/')

@app.route('/complete')
def completeit():
    if request.method == 'GET':
        item = session.get_item(request.args.get('item_id'))
        item['status']='Complete'
        session.save_item(item)
        return redirect('/')

if __name__ == '__main__':
    app.run()
