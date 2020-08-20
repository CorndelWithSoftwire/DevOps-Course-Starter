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

@app.route('/newitems', methods=['POST'])
def newitems():
    #capture the title of newitem using a form and pass it to the add_item function
    session.add_item(request.form.get('Title')) 
    #redirect to index page
    return redirect('/') 

if __name__ == '__main__':
    app.run()
