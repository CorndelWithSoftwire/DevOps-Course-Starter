from datetime import time
import pytest
from app.create_app import create_app
import time
from selenium import webdriver
from threading import Thread
from dotenv import find_dotenv, load_dotenv

@pytest.fixture(scope='module')
def test_app():
    # construct the new application
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    application = create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False)) 
    thread.daemon = True
    thread.start()
    yield application 

    # Tear Down
    thread.join(1) 
    
@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver

def test_task_journey(driver, test_app): 
    test_item_name = 'Finish selenium test'
    # this is to stop a connection issue that was causing intermittant failures
    time.sleep(3)
    driver.get('http://localhost:5000/')
    driver.find_element_by_id('item').send_keys(test_item_name)
    driver.find_element_by_id('submit').click()
    driver.find_element_by_id(test_item_name+'_complete').click()
    driver.find_element_by_id(test_item_name+'_delete').click()

    assert test_item_name not in driver.page_source