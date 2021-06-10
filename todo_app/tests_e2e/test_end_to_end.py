import os, pytest, app

from threading import Thread
from Mongo_db import delete_mongo_db
from mongo_config import Config
from dotenv import load_dotenv, find_dotenv

@pytest.fixture(scope='module')
def test_app():
    # Create the new DB & update the DB environment variable
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    test_db_name = "testing_database"
    Config.MONGO_DB = test_db_name
    # construct the new application
    application = app.create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app

    # Tear Down
    thread.join(1)
    delete_mongo_db(test_db_name)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import geckodriver_autoinstaller
import time


@pytest.fixture(scope="module")
def driver():
    geckodriver_autoinstaller.install()
    opts = webdriver.FirefoxOptions()
    opts.add_argument('--headless')
    with webdriver.Firefox(options=opts) as driver:
        yield driver

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'

    elem = driver.find_element_by_name("Title")
    elem.send_keys("test item")
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.find_element_by_name('todo_doing').click()
    assert "test item" in driver.page_source


