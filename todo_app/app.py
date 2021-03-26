
from flask import Flask, render_template, request, redirect, url_for, session
from todo_app.data import session_items

from todo_app.flask_config import Config
import requests
import os
app = Flask(__name__)
app.config.from_object(Config)
secret_key = os.getenv('SECRET_KEY')

api_key = os.getenv('TRELLO_API_KEY')
api_token = os.getenv('TRELLO_TOKEN')
board_id= os.getenv('TRELLO_BOARD_ID')
listid_todo = os.getenv('ID_LIST_TODO')
listid_doing = os.getenv('ID_LIST_DOING')
listid_done = os.getenv('ID_LIST_DONE')
listid_newlist = os.getenv('ID_LIST_NEWLIST')
cards_cardOne =os.getenv('CARDS_TODO_CARD_ONE')
cards_cardTwo =os.getenv('CARDS_TODO_CARD_TWO')
cards_cardThree =os.getenv('CARDS_TODO_CARD_THREE')
cards_trelloDone =os.getenv('CARDS_TRELLODONE_CARD')
cards_trelloBoard =os.getenv('CARDS_DEVOPSTRELLOBOARD')

@app.route('/')
def index():
    
    api_key = os.getenv('TRELLO_API_KEY')
    api_token = os.getenv('TRELLO_TOKEN')
    board_id= os.getenv('TRELLO_BOARD_ID')
    listid_todo = os.getenv('ID_LIST_TODO')
    listid_doing = os.getenv('ID_LIST_DOING')
    listid_done = os.getenv('ID_LIST_DONE')
    params= {'key': api_key, 'token': api_token}
    response =  requests.get(f'https://api.trello.com/1/boards/{board_id}/cards', params= params)
    print(response.text)
    items=[]
    for item in response.json():
        if item['idList'] ==listid_todo:
            status="ToDo"
        elif item['idList'] == listid_done:
            status ='Done'
        items.append({'id':item['id'], 'status':status, 'title': item['name']})

    return render_template('index.html', items=items)

@app.route('/additem', methods =["POST"])
def add_item():
    api_key = os.getenv('TRELLO_API_KEY')
    api_token = os.getenv('TRELLO_TOKEN')
    listid_todo = os.getenv('ID_LIST_TODO')
    listid_doing = os.getenv('ID_LIST_DOING')
    listid_done = os.getenv('ID_LIST_DONE')
    params= {'key':api_key, 'token':api_token, 'idList':listid_todo, 'name':request.form.get("title")}
    response = requests.Post(f'https://api.trello.com/1/cards', params= params)
#return redirect(url_for("index"))
    

# @app.route('/<id>')
# def get_item(id):
#     item = session_items.get_item(id)
#     return f"Item returned is {item['title']}"

# @app.route('/deleteitem', methods =["POST"])
# def delete_item():
#     id = request.form.get("id")
#     session_items.delete_item(id)
#     return redirect(url_for("index"))

@app.route('/account')
def getAccountDetails():
    #secret_key = os.environ('SECRET_KEY')
    api_key = os.getenv('TRELLO_API_KEY')
    api_token = os.getenv('TRELLO_TOKEN')
    board_id= os.getenv('TRELLO_BOARD_ID')
    params= {'key': api_key, 'token': api_token}
    response =  requests.get(f'https://api.trello.com/1/members/me/?{api_key}&{api_token}')
    #response =  requests.get(f'https://api.trello.com/1/members/me/?', params= params)
    print(response.text)
    print(response.json())

# @app.route('/allrequests')
# def getAllRequestsDetails():
#     secret_key = os.environ('SECRET_KEY')
#     api_key = os.getenv('TRELLO_API_KEY')
#     api_token = os.getenv('TRELLO_TOKEN')
#     board_id= os.getenv('TRELLO_BOARD_ID')
#     listid_todo = os.getenv('ID_LIST_TODO')
#     listid_doing = os.getenv('ID_LIST_DOING')
#     listid_done = os.getenv('ID_LIST_DONE')
#     listid_newlist = os.getenv('ID_LIST_NEWLIST')
#     cards_cardOne =os.getenv('CARDS_TODO_CARD_ONE')
#     cards_cardTwo =os.getenv('CARDS_TODO_CARD_TWO')
#     cards_cardThree =os.getenv('CARDS_TODO_CARD_THREE')
#     cards_trelloDone =os.getenv('CARDS_TRELLODONE_CARD')
#     cards_trelloBoard =os.getenv('CARDS_DEVOPSTRELLOBOARD')
#     params= {'key': api_key, 'token': api_token}
#     response =  requests.get(f'https://api.trello.com/1/boards/{board_id}', params= params)
#     #conn.request("GET", "/1/boards/6054b0101e6a3d49645dbdc8?key=2de5a83f280229944d5715d11c00ff59&token=0fdbf0ca6f756c091754bff9f5848a0591cd21212fddb27373ff332a6ed0f19c&board_id=6054b0101e6a3d49645dbdc8", payload, headers)
#     print(response.text)
#     print(response.json())

# @app.route('/list')
# def getListDetails():
#     secret_key = os.environ('SECRET_KEY')
#     api_key = os.getenv('TRELLO_API_KEY')
#     api_token = os.getenv('TRELLO_TOKEN')
#     listid_newlist = os.getenv('ID_LIST_NEWLIST')
#     board_id= os.getenv('TRELLO_BOARD_ID')
#     params= {'key': api_key, 'token': api_token}
#     response =  requests.get(f'https://api.trello.com/1/lists/{listid_newlist}', params= params)
#     #response =  requests.get(f'https://api.trello.com/1/members/me/?', params= params)
#     print(response.text)
#     print(response.json())

# @app.route('/doinglist')
# def getdoingListDetails():
#     secret_key = os.environ('SECRET_KEY')
#     api_key = os.getenv('TRELLO_API_KEY')
#     api_token = os.getenv('TRELLO_TOKEN')
#     listid_todo = os.getenv('ID_LIST_TODO')
#     listid_newlist = os.getenv('ID_LIST_NEWLIST')
#     listid_doing = os.getenv('ID_LIST_DOING')
#     listid_done = os.getenv('ID_LIST_DONE')
#     board_id= os.getenv('TRELLO_BOARD_ID')
#     params= {'key': api_key, 'token': api_token}
#     response =  requests.get(f'https://api.trello.com/1/lists/{listid_doing}', params= params)
#     #response =  requests.get(f'https://api.trello.com/1/members/me/?', params= params)
#     print(response.text)
#     print(response.json())

# @app.route('/card')
# def getcardDetails():
#     secret_key = os.environ('SECRET_KEY')
#     api_key = os.getenv('TRELLO_API_KEY')
#     api_token = os.getenv('TRELLO_TOKEN')
#     cards_cardOne =os.getenv('CARDS_TODO_CARD_ONE')
#     cards_cardTwo =os.getenv('CARDS_TODO_CARD_TWO')
#     listid_todo = os.getenv('ID_LIST_TODO')
#     listid_newlist = os.getenv('ID_LIST_NEWLIST')
#     listid_doing = os.getenv('ID_LIST_DOING')
#     listid_done = os.getenv('ID_LIST_DONE')
#     board_id= os.getenv('TRELLO_BOARD_ID')
#     params= {'key': api_key, 'token': api_token}
#     response =  requests.get(f'https://api.trello.com/1/cards/{cards_cardOne}', params= params)
#     #response =  requests.get(f'https://api.trello.com/1/members/me/?', params= params)
#     print(response.text)
#     print(response.json())


# @app.route('/movecard')
# def movecardDetails():
#     secret_key = os.environ('SECRET_KEY')
#     api_key = os.getenv('TRELLO_API_KEY')
#     api_token = os.getenv('TRELLO_TOKEN')
#     board_id= os.getenv('TRELLO_BOARD_ID')
#     listid_todo = os.getenv('ID_LIST_TODO')
#     listid_doing = os.getenv('ID_LIST_DOING')
#     listid_done = os.getenv('ID_LIST_DONE')
#     listid_newlist = os.getenv('ID_LIST_NEWLIST')
#     cards_cardOne =os.getenv('CARDS_TODO_CARD_ONE')
#     cards_cardTwo =os.getenv('CARDS_TODO_CARD_TWO')
#     cards_cardThree =os.getenv('CARDS_TODO_CARD_THREE')
#     cards_trelloDone =os.getenv('CARDS_TRELLODONE_CARD')
#     cards_trelloBoard =os.getenv('CARDS_DEVOPSTRELLOBOARD')
#     params= {'key': api_key, 'token': api_token}
#     response =  requests.put(f'https://api.trello.com/1/cards/{cards_cardOne}', params= params, {listid_doing})
#     #conn.request("PUT", "/1/cards/605a41e5ab231a6fd025c29a?key=2de5a83f280229944d5715d11c00ff59&token=0fdbf0ca6f756c091754bff9f5848a0591cd21212fddb27373ff332a6ed0f19c&idList=6054b0101e6a3d49645dbdca", payload, headers)
#     print(response.text)
#     print(response.json())


# @app.route('/createcard')
# def createcardDetails():
#     secret_key = os.environ('SECRET_KEY')
#     api_key = os.getenv('TRELLO_API_KEY')
#     api_token = os.getenv('TRELLO_TOKEN')
#     board_id= os.getenv('TRELLO_BOARD_ID')
#     listid_todo = os.getenv('ID_LIST_TODO')
#     listid_doing = os.getenv('ID_LIST_DOING')
#     listid_done = os.getenv('ID_LIST_DONE')
#     listid_newlist = os.getenv('ID_LIST_NEWLIST')
#     cards_cardOne =os.getenv('CARDS_TODO_CARD_ONE')
#     cards_cardTwo =os.getenv('CARDS_TODO_CARD_TWO')
#     cards_cardThree =os.getenv('CARDS_TODO_CARD_THREE')
#     cards_trelloDone =os.getenv('CARDS_TRELLODONE_CARD')
#     cards_trelloBoard =os.getenv('CARDS_DEVOPSTRELLOBOARD')
#     params= {'key': api_key, 'token': api_token}
#     response =  requests.post(f'https://api.trello.com/1/cards/{cards_cardOne}', params= params, {listid_doing})
#     #conn.request("POST", "/1/cards?key=2de5a83f280229944d5715d11c00ff59&token=0fdbf0ca6f756c091754bff9f5848a0591cd21212fddb27373ff332a6ed0f19c&name=ToDoCardThree&idList=6054b0101e6a3d49645dbdc9", payload, headers)
#     print(response.text)
#     print(response.json())
   
    


if __name__ == '__main__':
    app.run()
