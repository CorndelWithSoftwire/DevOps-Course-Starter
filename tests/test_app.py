import os
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

board_lists_json = [
    {
        "id": "5f4dfb5dc9f1a151051ce7a6",
        "name": "Todo"
    },
    {
        "id": "5f4dfb63e12bc1039a2bca84",
        "name": "Done"
    }
]


@pytest.fixture
def client():
    mock_get_request = patch('trello_request.requests.request')
    mock_get = mock_get_request.start()
    mock_get.return_value = _mock_response(json_data=board_lists_json)

    # Use our test integration config instead of the 'real' version file_path = find_dotenv('.env.test')
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()

    mock_get_request.stop()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client


@patch('trello_request.requests.request')
def test_index_page_with_todos(mock_get_requests, client):
    mock_resp = _mock_response(json_data=todos_json)
    mock_get_requests.return_value = mock_resp

    # When
    response = client.get('/')

    # Then
    assert b"Valid Item" in response.data
    assert b"Some other Item" in response.data
    assert b"An Item with a due" in response.data
    assert b"Sep 22" in response.data


@patch('trello_request.requests.request')
def test_add_item_with_a_todo(mock_post_request, client):
    # Given

    form_data = {
        "newitem": "Valid Item",
        "duedate": "2020-10-21"
    }

    # When
    client.post('/additem', data=form_data)

    # Then
    mock_post_request.assert_called_with('POST', 'https://api.trello.com/1/cards',
                                         params={'key': 'eiruty89457934iy', 'token': 'ijehgeriu835hghe8r9348hfi539h585terh5893', 'idList': '5f4dfb5dc9f1a151051ce7a6',
                                                 'name': 'Valid Item', 'due': '2020-10-21'})
