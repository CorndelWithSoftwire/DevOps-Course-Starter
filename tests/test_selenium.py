import os
import pytest
import time
import requests
from threading import Thread
from selenium import webdriver
from selenium.webdriver import Firefox
from dotenv import find_dotenv, load_dotenv
from selenium.webdriver.common.keys import Keys
from todo_app.app import create_app
from todo_app.trello_cards import create_a_board, delete_a_board, make_trello_auth
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="module")
def driver():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    with webdriver.Firefox() as driver:
        yield driver

def load_list():
    """ Simple attempt to get all cards from Trello. """
    request_url = make_trello_auth(f"https://api.trello.com/1/boards/{os.getenv('BOARD_ID')}/lists")
    response = requests.get(request_url)
    todos = response.json()
    for list in todos:
        print(list['name'], list['id'])
        if list['name'] == "To Do":
            os.environ['TODO_idList'] = list['id']
        if list['name'] == "Doing":
            os.environ['DOING_idList'] = list['id']
        if list['name'] == "Done":
            os.environ['DONE_idList'] = list['id']
    return list


@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    board_id = create_a_board('board_id')
    os.environ['BOARD_ID'] = board_id
    load_list()


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
    assert driver.title == 'To-Do App'

    # Create a task
    driver.find_element_by_name("name").send_keys("New Item")
    driver.find_element_by_name("desc").send_keys("New Description - Done")
    driver.find_element_by_class_name('btn-success').click()
    time.sleep(3)
    # assert ("New Description - Done" in driver.page_source)

    # Mark task as complete 
    driver.find_element_by_xpath("//*[contains(text(), 'Complete Item')]").click()
    # assert ("New Description - Done" in driver.page_source)

    # Delete the task
    driver.find_element_by_class_name('btn-danger').click()
    # assert "New Description - Done" not in driver.page_source
    driver.quit()
    
