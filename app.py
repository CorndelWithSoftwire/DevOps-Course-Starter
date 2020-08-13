from flask import Flask, render_template, request, redirect, url_for
import session_items as session
# import webbrowser

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    Items=session.get_items()   
   # session.add_item('A super entry')   # This works to add entries
    return render_template('index.html',passedItems=Items)

@app.route('/addentry', methods = ['GET','POST','DELETE'])
def entry():
    Titleback=request.form.get('title')
    return redirect("/")

if __name__ == '__main__':
   
#    app.run(host='http://127.0.0.1', port=port)
    app.run()
