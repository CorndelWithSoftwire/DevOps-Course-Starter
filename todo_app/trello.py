import requests
import json
import os
from todo_app.Task import Task

headers = {
   "Accept": "application/json"
}

def get_all_tasks():
    params = (
        ('key', os.environ['TRELLO_KEY']),
        ('token', os.environ['TRELLO_TOKEN']),        
    )
    board_id = os.environ['TRELLO_BOARD_ID']
    data = requests.get('https://api.trello.com/1/boards/' + board_id + '/cards', params=params).json()
    task_list = []
    for task in data:
        if task['idList'] == os.environ['TRELLO_TODO_LIST_ID']:
            task['idList'] = 'To Do'
        elif task['idList'] == os.environ['TRELLO_DOING_LIST_ID']:
            task['idList'] = 'Doing'
        elif task['idList'] == os.environ['TRELLO_DONE_LIST_ID']:
            task['idList'] = 'Done'
        
        task_list.append(Task(id=task['id'], status=task['idList'], title=task['name'], last_modified=task['dateLastActivity']))
        
    return task_list

def create_todo_task(title):
    params = (
        ('key', os.environ['TRELLO_KEY']),
        ('token', os.environ['TRELLO_TOKEN']),
        ('name', title),
        ('idList', os.environ['TRELLO_TODO_LIST_ID'])
    )
    print(os.environ['TRELLO_KEY'])
    print(os.environ['TRELLO_TOKEN'])
    print(os.environ['TRELLO_TODO_LIST_ID'])
    requests.post('https://api.trello.com/1/cards', params=params)

def move_to_doing(id):
    params = (
        ('key', os.environ['TRELLO_KEY']),
        ('token', os.environ['TRELLO_TOKEN']),
        ('idList', os.environ['TRELLO_DOING_LIST_ID'])
    )
    requests.put("https://api.trello.com/1/cards/" + id, params=params)

def move_to_done(id):    
    params = (
        ('key', os.environ['TRELLO_KEY']),
        ('token', os.environ['TRELLO_TOKEN']),
        ('idList', os.environ['TRELLO_DONE_LIST_ID'])
    )
    requests.put("https://api.trello.com/1/cards/" + id, params=params)

def delete_task(id):
    params = (
        ('key', os.environ['TRELLO_KEY']),
        ('token', os.environ['TRELLO_TOKEN'])
    )
    requests.delete("https://api.trello.com/1/cards/" + id, params=params)

def create_board():
    params = (
        ('key', os.environ['TRELLO_KEY']),
        ('token', os.environ['TRELLO_TOKEN']),
        ('name', 'TestBoard1')
    )
    response = requests.post("https://api.trello.com/1/boards/", params=params)
    return response.json()['id']

def delete_board(id):
    params = (
        ('key', os.environ['TRELLO_KEY']),
        ('token', os.environ['TRELLO_TOKEN'])
    )
    requests.delete("https://api.trello.com/1/boards/" + id, params=params)