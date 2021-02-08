import os
import random
from threading import Thread

from todoapp import app
from todoapp import common
import pytest
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from todoapp.trello_request import TrelloRequest


class TrelloCreateBoard(TrelloRequest):
    URL_PATH = "/boards"

    def create(self, board_name):
        url = self.URL_PATH

        query = {
            'name': board_name
        }

        json_data = super().makeRequest(url, "POST", query)

        return json_data['id']


class TrelloDeleteBoard(TrelloRequest):
    URL_PATH = "/boards/{}"

    def delete(self, board_id):
        url = self.URL_PATH.format(board_id)
        return super().makeRequest(url, "DELETE")


class TrelloCreateList(TrelloRequest):
    URL_PATH = "/lists"

    def create(self, name, board_id):
        url = self.URL_PATH

        query = {
            'name': name,
            'idBoard': board_id
        }

        json_data = super().makeRequest(url, "POST", query)

        return json_data['id']


def create_trello_board():
    name = f"Selenium Test Board {random.randint(100, 1000)}"
    return TrelloCreateBoard().create(name)


def delete_trello_board(board_id):
    return TrelloDeleteBoard().delete(board_id)


def createList(board_id, list_name):
    return TrelloCreateList().create(list_name, board_id)


@pytest.fixture(scope='module')
def test_app():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)

    # some load or setup issues with environment
    TrelloRequest.APP_TOKEN = os.getenv("APP_TOKEN")
    TrelloRequest.APP_API_KEY = os.getenv("APP_API_KEY")

    # Create the new board & update the board id environment
    board_id = create_trello_board()
    os.environ['TODO_BOARD_ID'] = board_id

    createList(board_id, common.Lists.TODO_LIST_NAME)
    createList(board_id, common.Lists.DONE_LIST_NAME)

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