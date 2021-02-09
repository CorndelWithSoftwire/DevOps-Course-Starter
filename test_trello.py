import os
import dotenv
import pytest
import app as app
import trello_items as trello
from threading import Thread 
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    trello_board_id = trello.create_trello_board("test_task_journey")
    lists_on_board = test_app.trello_items.getListsOnBoards(trello_board_id)
    test_app.trello_items.setListIdInEnv(lists_on_board)
    task_id = test_app.trello_items.add_item("test task")
    moved_to_inprogress = test_app.trello_items.inprogress_item(task_id)
    mark_as_done = test_app.trello_items.markAsDone(task_id )
    trello.delete_trello_board(trello_board_id)

    assert driver.title == 'To-Do App'
    assert task_id is not None
    assert moved_to_inprogress is True
    assert mark_as_done is True

def test_create_and_delete_board():
     trello_board_id = trello.create_trello_board("test_create_and_delete_board")
     board_deleted = trello.delete_trello_board(trello_board_id)

     assert trello_board_id is not None
     assert board_deleted is True
    
@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    board_id = trello.create_trello_board("TestAppBoard") 
    os.environ['trello_boardid'] = board_id
    # construct the new application
    application = app.create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app
    # Tear Down
    thread.join(1)
    trello.delete_trello_board(board_id)

@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver



