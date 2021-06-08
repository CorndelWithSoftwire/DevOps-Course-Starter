from os import environ, path
from threading import Thread
#from todo_app.data.trello import createNewBoard, deleteBoard
from todo_app import app
import pytest
from unittest.mock import patch, Mock
from selenium import webdriver
import os
from todo_app.data.trello  import Trello


@pytest.fixture(scope='module')
def app_with_temp_board():
    trello =Trello()
    # Create the new board & update the board idenvironment variable
    board_id = trello.createNewBoard('SeleniumNewBoard')
    os.environ['TRELLO_BOARD_ID'] = board_id
    # construct the new application
    application = app.create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda:
    application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app

    # Tear Down
    thread.join(1)
    trello.deleteBoard(board_id)

@pytest.fixture(scope= 'module')
def driver():
    # path to your webdriver download
    with webdriver.Chrome('C:/Support/Selenium Drivers/chromedriver.exe') as driver:
        yield driver 

def test_task_journey(driver,app_with_temp_board):
     driver.get('http://localhost:5000/')
     assert driver.title == 'To-Do App'
      # Trello_Base_Url = "https://trello.com/"
       #     Trello_title = 'Boards | Trello' C:/DevOpsWork/DevOps-Course-Starter/todo_app/SeleniumTest/drivers