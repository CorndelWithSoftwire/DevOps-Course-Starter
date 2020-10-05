import os

TRELLO_API_URL = 'https://api.trello.com/1/'
TRELLO_BOARD_ID = '5f6456f8fc414517ed9b0e41'
trello_key = os.getenv('TRELLO_KEY')
trello_token = os.getenv('TRELLO_TOKEN')
TRELLO_CREDENTIALS = f"key={trello_key}&token={trello_token}"

TRELLO_IDLIST = "idList"
TRELLO_ID_BOARD = 'idBoard'
TRELLO_ID = "id"
TRELLO_NAME = "name"

TRELLO_KEYS_PATH = "todo_app/trello_secrets.txt"
TODO_APP_NOT_STARTED = "Not Started"
TODO_APP_COMPLETED = "Completed"