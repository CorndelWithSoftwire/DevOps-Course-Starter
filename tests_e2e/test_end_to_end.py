import os, requests, pytest, app
from threading import Thread

from Trello_items import boardsurl, get_trello_key, get_trello_token, build_auth_query
from Trello_boards import create_trello_board, delete_trello_board
from dotenv import load_dotenv, find_dotenv

@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    board_id = create_trello_board()
    os.environ['TRELLO_TODO_BOARDID'] = board_id

    # construct the new application
    application = app.create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app

    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'

    elem = driver.find_element_by_name("Title")
    elem.send_keys("test item")
    elem.send_keys(Keys.RETURN)
    driver.implicitly_wait(2)
    driver.find_element_by_name('todo_doing').click()
    driver.implicitly_wait(2)
    driver.find_element_by_name('doing_complete').click()
    assert "test item" in driver.page_source

    

