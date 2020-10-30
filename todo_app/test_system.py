import os
import pytest
import todo_app.app as app
from todo_app.trello import create_board, delete_board
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import dotenv
import requests
 
@pytest.fixture(scope='module')
def test_app():

    file_path = dotenv.find_dotenv('.env') 
    dotenv.load_dotenv(file_path, override=True)      

    # Create the new board & set it to env variable
    board_id = create_board() 
    os.environ['TRELLO_BOARD'] = board_id

    # Get the new board list ids and update the environment variables
    params = (
        ('key', os.environ['TRELLO_KEY']),
        ('token', os.environ['TRELLO_TOKEN']),
        ('fields', 'all')
    )
    boardid = os.environ['TRELLO_BOARD']
    r = requests.get(f'https://api.trello.com/1/boards/' + boardid + '/lists', params=params)

    to_do_id = r.json()[0]['id']
    doing_id = r.json()[1]['id']
    done_id = r.json()[2]['id']

    os.environ['TRELLO_TODO_LIST_ID'] = to_do_id
    os.environ['TRELLO_DOING_LIST_ID'] = doing_id
    os.environ['TRELLO_DONE_LIST_ID'] = done_id

    # construct the new application   
    application = app.create_app()   

    # start the app in its own thread.  
    thread = Thread(target=lambda: application.run(use_reloader=False))  
    thread.daemon = True  
    thread.start()   
    yield app   

    # Tear Down     
    thread.join(1)  
    delete_board(board_id) 



@pytest.fixture(scope="module")
def driver():     
    with webdriver.Chrome() as driver:
        yield driver 

def test_adding_new_task(driver, test_app):
    driver.get('http://localhost:5000/')  
        
    input_field = driver.find_element_by_id('title')
    input_field.send_keys("TestTask")
    add_item = driver.find_element_by_id('new_task')
    add_item.click()    
    page_source = driver.page_source    
    assert "TestTask" in page_source