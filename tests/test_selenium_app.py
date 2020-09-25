import os
import random
from threading import Thread

from dotenv import find_dotenv, load_dotenv
from selenium import webdriver

import common

import pytest

import app
from trello_request import TrelloRequest


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
    TrelloRequest.APP_TOKEN=os.getenv("APP_TOKEN")
    TrelloRequest.APP_API_KEY=os.getenv("APP_API_KEY")

    # Create the new board & update the board id environment
    board_id = create_trello_board()
    os.environ['TODO_BOARD_ID'] = board_id

    todo_list_id = createList(board_id, common.Lists.TODO_LIST_NAME)
    done_list_id = createList(board_id, common.Lists.DONE_LIST_NAME)

    os.environ['TODO_LIST_ID'] = todo_list_id
    os.environ['DONE_LIST_ID'] = done_list_id

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
    with webdriver.Firefox() as driver:
        yield driver


def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'Quick and Dirty To-Do'

