import os
import requests
import todo_item

#from todo_item import TodoItem

board_id = os.getenv('TRELLO_BOARD_ID')
api_key = os.getenv('TRELLO_API_KEY')
api_secret = os.getenv('TRELLO_API_SECRET')
new_status_value = todo_item
not_started = os.getenv('NOT_STARTED')
in_progress = os.getenv('IN_PROGRESS')
completed = os.getenv('COMPLETED')


def get_cards():
    response = requests.get(f'http://api.trello.com/1/boards/{board_id}/cards', params ={'key': api_key, 'token': api_secret, })
    return response.json()

def get_cards_list(card_id):
    response = requests.get(f'https://api.trello.com/1/cards/{card_id}/list', params ={'key': api_key, 'token': api_secret})
    return response.json()

def get_lists():
    response = requests.get(f'http://api.trello.com/1/boards/{board_id}/lists', params ={'key': api_key, 'token': api_secret})
    return response.json()

def create_task(new_task_text):
    query={'key': api_key, 'token': api_secret, 'idList': not_started, 'name': new_task_text}
    response = requests.request(
        "POST",
        f"https://api.trello.com/1/cards",
        params = query
    )
    return response

def delete_todo(id):
    
    response = requests.delete(
        f"https://api.trello.com/1/cards/{id}", params ={'key': api_key, 'token': api_secret}
    )

    print(response.text)
    return response.json()
 
def update_todo(id, new_todo_value, new_status_value):
    
    url =  f"https://api.trello.com/1/cards/{id}/", 
    
    headers = {
        "Accept": "application/json"
    }
    query = {'key': api_key, 'token': api_secret, 'name': new_todo_value, 'idList': new_status_value}
    #print repsonses to help build code
    print (query)
    print(id)
    print(url)
    response = requests.request(
        "PUT", 
        url,  
        headers = headers,
        params = query
    )
    print (response.text)
    return response.json()
    



"""def update_todo(id, new_todo_value, new_status_value):
    headers = {
        "Accept": "application/json"
    }

    url = f"https://api.trello.com/1/cards/{id}"

    params = { "key": api_key,
                "token": api_secret,
                "value": {
                    'idList': new_status_value,
                    'name': new_todo_value
                }
            }
    
    response = requests.request(
        "PUT",
        url,
        headers = headers,
        json=params
    )
    print (response.text)
    return response.json()"""


