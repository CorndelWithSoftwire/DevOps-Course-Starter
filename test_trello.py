import os
import dotenv
import pytest
import app as app
import session_items as session
from threading import Thread 
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')

    assert driver.title == 'To-Do App'
    
@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    board_id = session.create_trello_board()
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
    session.delete_trello_board(board_id)

@pytest.fixture(scope="module")
def driver():

    with webdriver.Firefox() as driver:
        yield driver



