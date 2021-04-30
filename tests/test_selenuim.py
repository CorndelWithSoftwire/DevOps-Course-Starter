from threading import Thread

import mongomock
import pytest
from selenium import webdriver
from dotenv import find_dotenv, load_dotenv

from todo_app import app


@pytest.fixture(scope='module')
def test_app():
    with mongomock.patch(servers=('mongodb://example:27017/',)):
        file_path = find_dotenv('../.env.test')
        load_dotenv(file_path, override=True)
        # construct the new application
        application = app.create_app()
        # start the app in its own thread.
        thread = Thread(target=lambda: application.run(use_reloader=False))
        thread.daemon = True
        thread.start()
        yield app
        # Tear Down
        thread.join(1)
        print('Completed tests')


@pytest.fixture(scope="module")
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    with webdriver.Chrome('./chromedriver', options=opts) as driver:
        yield driver


def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')

    assert driver.title == 'To-Do App'

    driver.find_element_by_id('title').send_keys('test name')
    driver.find_element_by_id('desc').send_keys('test desc')
    driver.find_element_by_xpath('/html/body/div/div[3]/form/input[3]').click()
    todo_list = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/ul/li')
    assert 'test' in str(todo_list.text)

    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/ul/li/span/form/button').click()
    completed_list = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/ul/li[1]')
    assert 'test' in str(completed_list.text)
