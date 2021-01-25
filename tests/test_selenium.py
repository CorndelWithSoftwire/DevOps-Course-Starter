import os
import pytest
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from app import app
from trello_cards import create_a_board, delete_a_board

@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver


@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    board_id = create_a_board()
    os.environ['TRELLO_BOARD_ID'] = board_id

    # construct the new application
    application = app.create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app

    # Tear Down
    thread.join(1)
    delete_a_board(board_id)


search_page = driver.get('http://localhost:5000/')

def test_task_journey(driver, test_app): 

    search_page.load()
    assert driver.title == 'To-Do App'

