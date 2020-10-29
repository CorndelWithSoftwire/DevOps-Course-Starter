import os
import time
from threading import Thread
from flask import Flask, render_template, request, redirect, url_for, json
import requests
import unittest
from unittest.mock import patch
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import app
import config as cf

from dotenv import load_dotenv

@pytest.fixture(scope='module')
def test_app():
    load_dotenv(override=True)
    # Create the new board & update the board id environment variable
    board_id = create_trello_board('Testing')
    os.environ['BOARD_ID'] = board_id
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
    #driver.get('http://127.0.0.1:5000/')
    #assert driver.title == 'To-Do App' 
    driver.find_element_by_id('new_to_do_title').send_keys('New_To_Do_Selenium3')
    driver.find_element_by_id('new_to_do_submit').click()
    
    #time.sleep(10)
    #WebDriverWait(driver, 30).until(ec.url_matches('/'), 'add page still not refresh for response')
    #WebDriverWait(driver, 30).until(ec.url_matches('/add'), 'add page still not refresh for response')
    WebDriverWait(driver, 30).until(ec.text_to_be_present_in_element((By.ID, "list_of_to_dos"), "New_To_Do_Selenium3"))

    #assert 'New_To_Do_Selenium' in driver.find_element_by_id('To_Do_ul').text

    selenium_to_do_items = driver.find_elements_by_xpath("//div[@id='list_of_to_dos']/ul/li")
    #selenium_all_list_items = driver.find_elements_by_class_name("list-group mb-4")
    
    for item in selenium_to_do_items:
        print(item.text)

    content = driver.page_source

    print(content)

    print('About to execute Final Assert ')
    assert driver.title == 'To-Do App' 
    #assert url_for(test_app.trello_bp.index) in driver.current_url
    assert 'New_To_Do_Selenium3' in content


def create_trello_board(board_name):
    url = "https://api.trello.com/1/boards/"
    query = cf.get_trello_query()
    query['name'] = board_name

    response = requests.request(  "POST", url, params=query )
    return json.loads(response.text)['id']

def delete_trello_board(board_id):
    url = "https://api.trello.com/1/boards/{id}"

    query = cf.get_trello_query()
    query['id'] = board_id

    response = requests.request( "DELETE",  url, params=query )
    print(response.text)