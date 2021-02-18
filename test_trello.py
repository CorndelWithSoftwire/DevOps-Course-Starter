import os
import dotenv
import pytest
import requests
import app as app
import trello_items as trello
from threading import Thread 
import time
import unittest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    
    task_id = test_app.trello_items.add_item("test task")
    moved_to_inprogress = test_app.trello_items.inprogress_item(task_id)
    mark_as_done = test_app.trello_items.markAsDone(task_id )

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
    file_path = dotenv.find_dotenv('.env')    
    # Create the new board & update the board id environment variable
    board_id = trello.create_trello_board("TestAppBoard") 
    os.environ['trello_boardid'] = board_id

    params = (
        ('key', os.environ['trello_key']),
        ('token', os.environ['trello_token']),
        ('fields', 'all')
    )

    r = requests.get('https://api.trello.com/1/boards/' + os.environ['trello_boardid'] + '/lists', params=params)

    os.environ['todo_list_id'] = r.json()[0]['id']
    os.environ['doing_list_id']  = r.json()[1]['id']
    os.environ['done_list_id'] = r.json()[2]['id']

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

def test_createTask(driver, test_app):
    driver.get('http://localhost:5000/')
    driver.find_element_by_id("addTask").send_keys("raj is the best")
    driver.find_element_by_id("submit").click()
    text = driver.find_elements_by_xpath("//*[contains(text(), 'raj is the best')]")
    time.sleep(2)
    assert len(text) > 0

