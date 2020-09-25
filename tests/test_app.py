from unittest.mock import patch

import pytest
from dotenv import load_dotenv, find_dotenv

import app


def _mock_response(
        status=200,
        content="CONTENT",
        json_data=None,
        raise_for_status=None):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        def raise_for_status(self):
            return True

    return MockResponse(json_data=json_data, status_code=status)


@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version file_path = find_dotenv('.env.test')
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client


@patch('trello_request.requests.request')
def test_index_page_with_todos(mock_get_requests, client):
    todos_json = [
        {
            "id": "5f57f133fe6fec1ff7e25d63",
            "dateLastActivity": "2020-09-21T17:39:25.603Z",
            "name": "Valid Item",
            "due": None
        },
        {
            "id": "5f57f133fe6fec1ff7e25d64",
            "dateLastActivity": "2020-09-21T17:39:25.603Z",
            "name": "Some other Item",
            "due": None
        },
        {
            "id": "5f57f133fe6fec1ff7e25d65",
            "dateLastActivity": "2020-09-21T17:39:25.603Z",
            "name": "An Item with a due",
            "due": "2020-09-22T10:00:00.603Z"
        }
    ]
    mock_resp = _mock_response(json_data=todos_json)
    mock_get_requests.return_value = mock_resp
    response = client.get('/')

    assert b"Valid Item" in response.data
    assert b"Some other Item" in response.data
    assert b"An Item with a due" in response.data
    assert b"Sep 22" in response.data

# @patch('trello_request.requests.request')
# def test_add_item_with_a_todo(mock_post_request, client):
#     todos_json = {
#             "id": "5f57f133fe6fec1ff7e25d63",
#             "dateLastActivity": "2020-09-21T17:39:25.603Z",
#             "name": "Valid Item",
#             "due": None
#         }
#
#     response = client.post('/additem')
#     mock_post_request.assert_called_with('/cards')
