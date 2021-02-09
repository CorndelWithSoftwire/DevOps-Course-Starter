from dotenv import find_dotenv, load_dotenv
import todo_app.app as app
import pytest
import os
from unittest.mock import patch, Mock

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

@patch('requests.get')
def test_index_page(mock_get_requests, client):
# Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect = mock_get_cards
    response = client.get('/')
    assert response.status_code == 200
    assert "some todo" in response.data.decode()

def mock_get_cards(url):
    if url == f'https://api.trello.com/1/boards/{os.getenv("BOARD_ID")}/cards?key={os.getenv("TRELLO_API_KEY")}&token={os.getenv("TRELLO_API_TOKEN")}':
        response = Mock()
        # sample_trello_lists_response should point to some test response data
        response.json.return_value = sample_trello_cards_response()
        return response
    return None

def sample_trello_cards_response():
    return [
        {
            "id": "some trello id",
            "name": "some todo",
            "desc": "A really good description",
            "idList": os.getenv('TODO_idList')
        }
    ]
    