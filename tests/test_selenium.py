import os
import pytest
from threading import Thread
from selenium import webdriver
from selenium.webdriver import Firefox
from dotenv import find_dotenv, load_dotenv
from selenium.webdriver.common.keys import Keys
from todo_app.app import create_app
from todo_app.trello_cards import create_a_board, delete_a_board
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="module")
def driver():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    with webdriver.Firefox() as driver:
        yield driver



@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    board_id = create_a_board('testboard')
    os.environ['TRELLO_BOARD_ID'] = board_id

    # construct the new application
    application = create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    # Tear Down
    thread.join(1)
    delete_a_board(board_id)


def test_task_journey(driver, test_app): 


    driver.get('http://localhost:5000/')
    # To_do: Create a task, Move it along, and delete the task
    add_new_item = driver.find_element_by_name("name")
    add_description = driver.find_element_by_name("desc")
    submit = driver.find_element_by_class_name('btn-success')
  

    add_new_item.send_keys("New item")
    add_description.send_keys("New Description")
    # submit.click()

    assert driver.title == 'To-Do App'

