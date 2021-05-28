
from os import environ, path
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import pytest
from unittest.mock import patch, Mock
from todo_app.tests.unit.mockTrello_data import mock_get

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be  used in our tests.
    with test_app.test_client() as client:
        yield client

@patch('requests.get')
def test_index_page(mock_get_requests, client):
# Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect = mock_get_lists
    response = client.get('/')

    
def mock_get_lists(url, params):
    if url == f'https://api.trello.com/1/boards/boardid/cards':
        response = Mock()
# sample_trello_lists_response should pointto some test response data
         #response.json.return_value =sample_trello_lists_response()
        response.json.return_value = mock_get('GET', url)
        return response
    return None
  