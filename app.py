from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import trello_service as trello



app = Flask(__name__)
app.config.from_object('flask_config.Config')


@app.route('/')
def index():
    return render_template('index.html', items=sorted(session.get_items(), key=lambda item: item['status'], reverse=True))

@app.route('/trello')
def trello_page():
    return render_template('trello.html', cards=trello.get_all_cards())

@app.route('/addit', methods=['POST'])
def add_todo():
        session.add_item(request.form.get('new_item'))
        return redirect('/')

@app.route('/board/<name>')
def get_board(name):
    return trello.get_board_by_name(name)

@app.route('/list/<name>')
def get_list(name):
    return trello.get_list_by_name(name)

@app.route('/cards/<name>')
def get_cards_list(name):
    return trello.get_cards_by_list_name(name)

@app.route('/boards/all')
def get_all_board():
    return trello.get_all_boards()

@app.route('/lists/all')
def get_all_lists():
    return trello.get_all_lists()

@app.route('/card/new', methods=['POST'])
def add_card():
    name = request.form['new_card']
    trello.add_card_by_name(name)
    return redirect('/trello')

@app.route('/card/move', methods=['POST'])
def move_card():
    card_id = request.form['card_id']
    to_list = request.form['to_list']
    trello.move_card_to_new_list(card_id, to_list)
    return redirect('/trello')

@app.route('/complete')
def completeit():
    if request.method == 'GET':
        item = session.get_item(request.args.get('item_id'))
        item['status']='Complete'
        session.save_item(item)
        return redirect('/')

if __name__ == '__main__':
    app.run()
