import os

TRELLO_API_URL = 'https://api.trello.com/1/'
trello_key = os.getenv('TRELLO_KEY')
trello_token = os.getenv('TRELLO_TOKEN')
trello_default_board = os.getenv('TRELLO_BOARD_ID')
TRELLO_CREDENTIALS = f"key={trello_key}&token={trello_token}"
TRELLO_BOARD_ID = trello_default_board

TRELLO_IDLIST = "idList"
TRELLO_ID_BOARD = 'idBoard'
TRELLO_ID = "id"
TRELLO_NAME = "name"

TRELLO_KEYS_PATH = "todo_app/trello_secrets.txt"
TODO_APP_NOT_STARTED = "To Do"
TODO_APP_COMPLETED = "Done"