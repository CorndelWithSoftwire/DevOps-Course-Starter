import os
import dotenv
import pytest
import requests
import app as app
import mongo_items as mongo
from threading import Thread 
import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    
    task_id = test_app.mongo_items.add_item("test task")
    moved_to_inprogress = test_app.mongo_items.inprogress_item(task_id)
    mark_as_done = test_app.mongo_items.markAsDone(task_id)

    assert driver.title == 'To-Do App'
    assert task_id is not None
    assert moved_to_inprogress is True
    assert mark_as_done is True

def test_create_and_delete_board():
     database_id = mongo.create_database('test-db')
     database_deleted = mongo.delete_database('test-db')

     assert database_id is not None
     assert database_deleted is True
    

@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    mongo.create_database("TestAppBoard") 
    os.environ['MONGO_DB_NAME'] = "TestAppBoard"
    os.environ['MONGO_LIST_TODO'] = 'todo'
    os.environ['MONGO_LIST_INPROGRESS']  = 'inprogress'
    os.environ['MONGO_LIST_DONE'] = 'done'

    # construct the new application
    application = app.create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app
    # Tear Down
    thread.join(1)
    mongo.delete_database("TestAppBoard")

@pytest.fixture(scope="module")
# def driver():
#     with webdriver.Firefox() as driver:
#         yield driver
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome(ChromeDriverManager().install(), options=opts) as driver:
        yield driver

def test_createTask(driver, test_app):
    driver.get('http://localhost:5000/')
    driver.find_element_by_id("addTask").send_keys("raj is the best")
    driver.find_element_by_id("submit").click()
    text = driver.find_elements_by_xpath("//*[contains(text(), 'raj is the best')]")
    time.sleep(2)
    assert len(text) > 0

