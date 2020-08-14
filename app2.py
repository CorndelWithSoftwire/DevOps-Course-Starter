from flask import Flask, render_template, request, redirect, url_for
import requests
import session_items as session
# import webbrowser
from Package1 import Module2
trellokey=Module2.key             # get the key
trellotoken=Module2.token         # get the token
url = "https://api.trello.com/1/cards"
print (trellokey)               # testing purposes
print (trellotoken)             # testing purposes
print (url)                     # testing purposes
app = Flask(__name__)
app.config.from_object('flask_config.Config')

query = {
    'key': trellokey,
    'token': trellotoken,
    'idList': '5f352898dc8a8c31a0a1e439',
    'name': 'First added action'
}

@app.route('/')
def index():
    print ("Main application successfully refreshed")
    Items=session.get_items()   

    return render_template('index.html',passedItems=Items)

@app.route('/addentry', methods = ["POST"])
def entry():
    # Titleback=request.form.get('title')
    # Lets try putting the Trello thing in here.  First QUERY is what we're gonna send to the API
    query = {
        'key': trellokey,
        'token': trellotoken,
        'idList': '5f352898dc8a8c31a0a1e439',
     #   'name': 'First added action'                # hard coding at the start to check it works
        'name': request.form['title']
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )


    return redirect("/")




if __name__ == '__main__':
   
#    app.run(host='http://127.0.0.1', port=port)
    app.run()
