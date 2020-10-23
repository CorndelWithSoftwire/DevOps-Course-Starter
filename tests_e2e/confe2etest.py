import os
from dotenv import load_dotenv, find_dotenv
import pytest
from threading import Thread
from selenium import webdriver

from todo_app.data.trello_items import Trello_service
from todo_app import app

@pytest.fixture(scope='module')
def test_app():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    # Create the new board & update the board id environment variable
    service = Trello_service()
    board_id = service.create_board("E2E Test board")
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
    service.delete_board(board_id)

@pytest.fixture(scope='module')
def driver():
    with webdriver.Firefox() as driver:
        yield driver
