from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        item_title = request.form['Title']
        session.add_item(item_title)
        return redirect('/')
    else:
        items_list = session.get_items()
        # print(items_list)
        return render_template('index.html', items_list=items_list)

@app.route('/delete/<int:id>')
def delete(id):
    print('id', id)
    session.delete_item(id)
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    k = session.get_item(id)

    if request.method == 'POST':
        
        k['status'] = request.form['Status']
        k['title'] = request.form['Title']
        session.save_item(k)
        return redirect('/')

    else:
        
        # print(items_list)
        return render_template('update.html', k=k)

if __name__ == '__main__':
    app.run()
