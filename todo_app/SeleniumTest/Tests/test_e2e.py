from os import environ, path
from threading import Thread
from todo_app import app
import pytest
from unittest.mock import patch, Mock
from selenium import webdriver



# @pytest.fixture(scope='module')
# def app_with_temp_board():
# # Create the new board & update the board idenvironment variable
#     board_id = create_trello_board()
#     os.environ['TRELLO_BOARD_ID'] = board_id
# # construct the new application
#     application = app.create_app()
# # start the app in its own thread.
#     thread = Thread(target=lambda:
#     application.run(use_reloader=False))
#     thread.daemon = True
#     thread.start()
#     yield app

# # Tear Down
# thread.join(1)
# delete_trello_board(board_id)

# def test_task_journey(driver, app_with_temp_board):
# driver.get('http://localhost:5000/')
# assert driver.title == 'To-Do App'