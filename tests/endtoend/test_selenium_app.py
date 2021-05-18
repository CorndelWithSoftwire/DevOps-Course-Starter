import os
from threading import Thread

import pytest
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver

from todoapp import app
from todoapp.mongo_database import MongoDatabase


@pytest.fixture(scope='module')
def test_app():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=False)

    DB_URL = os.getenv("DB_URL")
    print(f"DB_URL: [{DB_URL}]")

    # construct the new application
    application = app.create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app
    # Tear Down
    thread.join(1)

    MongoDatabase().drop_database()


@pytest.fixture(scope="module")
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    with webdriver.Firefox(options=options) as driver:
        yield driver


def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'Quick and Dirty To-Do'

    # Create an item
    todo_item = 'Testing a todo item'
    input_element = driver.find_element_by_id("newitem")
    input_element.send_keys(todo_item)
    input_element.submit()

    driver.implicitly_wait(2)  # seconds

    # assert to see if its in to do section
    todo_item_label_element = driver.find_element_by_xpath("//div[@id='todoBlock']//label[@class='checkboxLabel']").text
    assert todo_item == todo_item_label_element

    # mark item as complete
    driver.find_element_by_xpath("//div[@id='todoBlock']//form/label[@class='checkboxLabel']").click()

    driver.implicitly_wait(2)  # seconds

    # assert to see its in done section
    todo_item_label_element = driver.find_element_by_xpath("//div[@id='doneBlock']//label[@class='checkboxLabel']").text
    assert todo_item == todo_item_label_element

    # move back to to do
    driver.find_element_by_xpath("//div[@id='doneBlock']//label[@class='checkboxLabel']").click()

    # assert to see if its in to do section
    todo_item_label_element = driver.find_element_by_xpath("//div[@id='todoBlock']//label[@class='checkboxLabel']").text
    assert todo_item == todo_item_label_element

    # delete item
    driver.find_element_by_xpath("//div[@id='todoBlock']//form/input[@alt='Delete']").click()

    # assert that its not there
    assert driver.page_source.find(todo_item) == -1