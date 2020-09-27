import os
from threading import Thread

import pytest
from selenium import webdriver
from dotenv import find_dotenv, load_dotenv

import app
import trello_boards
from flask_config import Config
from trello_boards import TrelloBoard


@pytest.fixture(scope='module')
def test_app():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    # Create the new board & update the board id environment variable
    create_board_response = trello_boards.create_board('sel_test_board')
    board_id = create_board_response.json()['id']
    os.environ['TRELLO_BOARD_ID'] = board_id
    # Set board list ids
    board_lists = trello_boards.get_lists_in_board(board_id)
    trello_board = TrelloBoard(board_lists.json())
    todo_id = trello_board.list_id('To Do')
    done_id = trello_board.list_id('Done')
    Config.LIST_ID = todo_id
    Config.DONE_LIST_ID = done_id
    # construct the new application
    application = app.create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app
    # Tear Down
    thread.join(1)
    trello_boards.delete_board(board_id)


@pytest.fixture(scope="module")
def driver():
    with webdriver.Chrome('/usr/local/bin/chromedriver') as driver:
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
