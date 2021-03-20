import os
import tempfile
import requests
import dotenv
import pytest
from flask import Flask, render_template, request, redirect, url_for, session
import mongo_items as mongo
import app as app
import datetime
from threading import Thread 
from unittest.mock import Mock, patch

today = datetime.date.today()
thingstodo = [{
        "_id": "123456",
        "name": "Another Task",
        "dateLastActivity": today.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        "idList": "test"
    }]


@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = dotenv.find_dotenv('.env.test')
    dotenv.load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

@patch('requests.get')
def test_index_page(mock_get_requests, client):
    mock_get_requests.side_effect = mock_get_cards
    response = client.get('/tasks')

    assert "Another Task" in response.data.decode() 
    assert "123456" in response.data.decode() 

def mock_get_cards(url, params):
       #TRELLO_BOARD_ID = os.environ.get("trello_boardid")

       #if url == f"https://api.trello.com/1/boards/{TRELLO_BOARD_ID}/cards":
              response = Mock()
              response.status_code = 200
              response.json.return_value = thingstodo 
              return response
       #return None
