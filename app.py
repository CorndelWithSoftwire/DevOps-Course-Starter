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
    """
    App using Trello API 
    """
    return render_template('trello.html', cards=trello.get_all_cards())

@app.route('/addit', methods=['POST'])
def add_todo():
        session.add_item(request.form.get('new_item'))
        return redirect('/')

@app.route('/card/new', methods=['POST'])
def add_card():
    """
    Adding new Trello card
    """
    name = request.form['new_card']
    trello.add_card_by_name(name)
    return redirect(url_for('trello_page'))

@app.route('/card/move', methods=['POST'])
def move_card():
    """
    Moving new Trello card
    """
    card_id = request.form['card_id']
    to_list = request.form['to_list']
    trello.move_card_to_new_list(card_id, to_list)
    return redirect(url_for('trello_page'))

@app.route('/complete')
def complete_item():
    if request.method == 'GET':
        item = session.get_item(request.args.get('item_id'))
        item['status']='Complete'
        session.save_item(item)
        return redirect('/')

if __name__ == '__main__':
    app.run()
