import os
from threading import Thread
from flask import Flask, render_template, request, redirect, url_for
import requests
import unittest
from unittest.mock import patch
import pytest
import pytest_html
from selenium import webdriver
import app
import config as cf

@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    board_id = create_trello_board('Testing')
    os.environ['TRELLO_BOARD_ID'] = board_id
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

#Fixture for Firefox
@pytest.fixture(scope="module")
def driver(request):
    ff_driver = webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App' 


def create_trello_board(board_name):
    url = "https://api.trello.com/1/boards/"
    query = cf.get_trello_query()
    query['name'] = board_name

    response = requests.request(  "POST", url, params=query )
    return response['id']

def delete_trello_board(board_id):
    url = "https://api.trello.com/1/boards/{id}"

    query = cf.get_trello_query()
    query['id'] = board_id

    response = requests.request( "DELETE",  url, params=query )
    print(response.text)