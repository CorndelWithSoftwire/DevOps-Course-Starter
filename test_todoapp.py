import os
import tempfile
import mock
import requests
import dotenv
import pytest
from flask import Flask, render_template, request, redirect, url_for, session
import trello_items as trello
import app as app
import datetime
from threading import Thread 
from unittest.mock import Mock

today = datetime.date.today()
thingstodo = [{
        "id": "123456",
        "title": "Another Task",
        "time": str(today),
        "status": "Things To Do"
    }]
lists = [{
        "id": "1",
        "name": "Things To Do"
    },{
        "id": "2",
        "name": "Doing"
    },{
        "id": "3",
        "name": "Done"
    },
    ]


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

@mock.patch('requests.get')
def test_index_page(mock_get_requests, client):
    mock_get_requests.side_effect = mock_get_cards
    response = client.get('/')

    assert response.status_code == 302

def mock_get_cards(url):
       TRELLO_BOARD_ID = os.environ.get("trello_boardid")
       API_KEY = os.environ.get("trello_key")
       TOKEN = os.environ.get("trello_token")
       if url == f"https://api.trello.com/1/boards/"+TRELLO_BOARD_ID+"/cards?key="+API_KEY+"&token="+TOKEN:
              print("URL was hit")
              response = Mock()
              response.status_code = 200
              response.json.return_value = sample_trello_cards_response 
              return response
       return None