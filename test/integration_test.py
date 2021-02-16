import pytest
from requests.models import Response
from app.create_app import create_app
from dotenv import find_dotenv, load_dotenv
from unittest.mock import Mock, patch

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version 
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    #Create the new app.
    test_app = create_app()
    
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client: 
        yield client

@patch('requests.get')
def test_index_page(mock_get_requests, client):
    mock_item_response = Response()
    mock_item_response.status_code = 200
    mock_item_response._content = b'[{"id": "123", "idList": "987", "name": "Why hello there", "dateLastActivity": "2021-01-06T21:14:06.518Z"}]'

    mock_list_response = Response()
    mock_list_response.status_code = 200
    mock_list_response._content = b'[{"id": "987", "name": "Done"}]'

    mock_get_requests.side_effect = [mock_item_response, mock_list_response]

    response = client.get('/')
    assert 200 == response.status_code
    assert "Why hello there" in response.data.decode()
    