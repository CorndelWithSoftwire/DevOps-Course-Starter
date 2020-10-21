import os.path
import os
import requests
from flask import Flask,escape,request,Response,render_template, redirect,url_for
import todo_app.data.session_items as session

app = Flask(__name__)
key = os.getenv("TRELLO_KEY")
token = os.getenv("TRELLO_TOKEN")
headers = {
   "Accept": "application/json"
}

def get_tasks(s_id):
    url = f"https://api.trello.com/1/lists/{s_id}/cards"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)
    data = [] 
    response_json = response.json()
    for a in response_json:
        data.append({'id': a['id'], 'name': a['name']}) 
    return data


def get_board(id):
    url = f"https://api.trello.com/1/boards/{id}"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)
    response_json = response.json()
    board = {"id": id, "name": response_json['name'] }    
    return board

def get_statuses(id):
    url = f"https://api.trello.com/1/boards/{id}/lists"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)  
    data = [] 
    response_json = response.json()
    for a in response_json:
        data.append({'id': a['id'], 'name': a['name']}) 
    return data

def get_task(id):
    url = f"https://api.trello.com/1/cards/{id}"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)    
    response_json = response.json()    
    task = {'id': response_json['id'], 'name': response_json['name'], 'status_id': response_json['idList'], 'board_id':response_json['idBoard'] }
    return task

def delete_task_id(id):
    url = f"https://api.trello.com/1/cards/{id}"
    querystring = {"key": key, "token": token}
    response = requests.request("DELETE", url, params=querystring)
    return response.text

def create_task(status_id, task_name):
    url = f"https://api.trello.com/1/cards"
    querystring = {"name": task_name, "idList": status_id, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring).json()
    task_id = response["id"]
    return task_id

def move_task_status(status_id, task_id):
    url = f"https://api.trello.com/1/cards/{task_id}"
    querystring = {"id": task_id, "idList": status_id, "key": key, "token": token}
    response = requests.request("PUT", url, params=querystring).json()
    task_id = response["id"]
    return task_id

def create_status(board_id, status_name):
    statuses = get_statuses(board_id)
    exists = False
    for status in statuses:
        if (status_name == status['name']):
            exists = True
    if (exists == False):
        url = f"https://api.trello.com/1/boards/{board_id}/lists"
        querystring = {"name": status_name, "key": key, "token": token}
        response = requests.request("POST", url, headers=headers, params=querystring).json()
        status_id = response["id"]
        return status_id

def create_board(board_name):
    url = "https://api.trello.com/1/boards/"
    querystring = {"name": board_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring).json()
    board_id = response["shortUrl"].split("/")[-1].strip()
    return board_id

def delete_board_id(id):
    url = f"https://api.trello.com/1/boards/{id}"
    querystring = {"key": key, "token": token}
    response = requests.request("DELETE", url, params=querystring)    
    return response.text

def delete_status_id(id):
    url = f"https://api.trello.com/1/boards/{id}/lists/{id}"
    querystring = {"key": key, "token": token}
    response = requests.request("DELETE", url, params=querystring)
    return response.text


@app.route('/add_board', methods=['GET', 'POST'])
def add_board():    
    if request.method == 'POST':
        board_name = request.form['board_name']                
        create_board(board_name)
        return redirect(url_for('index'))
    else:        
        return render_template("add_board.html")

@app.route('/delete_board')
def delete_board():
    board_id = request.args.get('id')  
    delete_board_id(board_id)
    return redirect(url_for('index'))

@app.route('/add_status', methods=['GET', 'POST'])
def add_status():    
    if request.method == 'POST':
        board_id = request.form['board_id']
        status_name = request.form['status_name']
        create_status(board_id, status_name)
        return redirect(url_for('view_board', id=board_id))
    else:
        board_id = request.args.get('board_id')
        board = get_board(board_id)    
        return render_template("add_status.html", board=board)


@app.route('/add_task', methods=['GET', 'POST'])
def add_task():    
    if request.method == 'POST':
        task_name = request.form['task_name']
        status_id = request.form['status_id']
        board_id = request.form['board_id']         
        create_task(status_id, task_name)
        return redirect(url_for('view_board', id=board_id))
    else:
        board_id = request.args.get('board_id')
        statuses = get_statuses(board_id)
        return render_template("add_task.html", board_id=board_id, statuses=statuses)

@app.route('/move_task', methods=['GET', 'POST'])
def move_task():
    if request.method == 'POST':
        id = request.form['id']        
        board_id = request.form['board_id'] 
        status_id = request.form['status_id']                       
        move_task_status(status_id, id)
        return redirect(url_for('view_board', id=board_id))
    else:
        board_id = request.args.get('board_id')
        task_id = request.args.get('task_id')
        statuses = get_statuses(board_id)
        task = get_task(task_id)        
        return render_template("move_task.html", task=task, statuses=statuses)


@app.route('/delete_task')
def delete_task():
    task_id = request.args.get('task_id')    
    board_id = request.args.get('board_id')
    delete_task_id(task_id)
    return redirect(url_for('view_board', id=board_id))


@app.route('/delete_status')
def delete_status():
    status_id = request.args.get('status_id')    
    board_id = request.args.get('board_id')
    delete_status_id(status_id)
    return redirect(url_for('view_board', id=board_id))


@app.route('/view_board', methods=['GET', 'POST'])
def view_board():
    id = request.args.get('id')    
    board = get_board(id)
    statuses = get_statuses(id)
    tasks = []
    for status in statuses:
        s_id = status['id']
        s_name = status['name']
        s_tasks = get_tasks(s_id)
        for task in s_tasks:
            tasks.append({'id': task['id'], 'name': task['name'], 's_id': s_id, 's_name': s_name})    
    return render_template("trello.html", board=board, statuses=statuses, tasks=tasks)

@app.route('/', methods=['GET', 'POST'])
def index():
    #items = session.get_items()
    url = "https://api.trello.com/1/members/me/boards"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)
    data = [] 
    json_data = response.json()
    for entry in json_data:
        data.append({'id': entry['id'], 'name': entry['name']}) 
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.debug = True
    app.run()


