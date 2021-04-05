import pytest
import todo_app.app as app
import dotenv
import requests
import json
import os
import datetime
from unittest.mock import MagicMock
from todo_app.mongo_db_tasks import TasksDb
from todo_app.Task import Task

@pytest.fixture
def client():

    # Use our test integration config instead of the 'real' version
    file_path = dotenv.find_dotenv('.env.test') 
    dotenv.load_dotenv(file_path, override=True)    
    
    # Create the new app.     
    
    taskDb = TasksDb()
    taskDb.get_all_tasks = MagicMock()
    taskDb.get_all_tasks.return_value = [        
        Task(id='604fabbef6dcb41ee250c4b6', status='To Do', title='TestTask', last_modified='2021-04-04 18:50:33.252000'),
        Task(id='604fac79f6dcb41ee250c4b9', status='To Do', title='TestTask2', last_modified='2021-04-04 18:50:33.252000')        
    ]

    test_app = app.create_app(taskDb)

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client: 
        yield client 

def test_index_page(client):
    response = client.get('/')
    response_html = response.data.decode()
    assert "TestTask" in response_html