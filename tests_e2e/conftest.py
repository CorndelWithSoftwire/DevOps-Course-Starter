import os
from attr import setters
from dotenv import load_dotenv, find_dotenv
import pytest
from threading import Thread
from selenium import webdriver

from todo_app.data.trello_items import Trello_service
from todo_app import app
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome('./chromedriver', options=opts) as driver:
        yield driver

@pytest.fixture(scope="module")
def test_app(driver):
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    # Create the new board & update the board id environment variable
    service = Trello_service()
    service.initiate()
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


