from unittest.mock import patch, MagicMock

import mongomock as mongomock
import pytest
from dotenv import load_dotenv, find_dotenv

from todoapp import app, mongo_database
from todoapp.common import Lists

MONGO_DB_URL = "mongodb://fakeuser:fakepass@servername:9999/testdb"


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
        "last_modified": "2020-09-21T17:39:25.603Z",
        "title": "Valid Item",
        "duedate": None
    },
    {
        "id": "5f57f133fe6fec1ff7e25d64",
        "last_modified": "2020-09-21T17:39:25.603Z",
        "title": "Some other Item",
        "duedate": None
    },
    {
        "id": "5f57f133fe6fec1ff7e25d65",
        "last_modified": "2020-09-21T17:39:25.603Z",
        "title": "An Item with a due",
        "duedate": "2020-09-22T10:00:00.603Z"
    }
]


@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version file_path = find_dotenv('.env.test')
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()

    test_app.config["LOGIN_DISABLED"] = True

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client


def test_index_page_with_todos(client):

    with patch.object(mongo_database.MongoDatabase, "client", mongomock.MongoClient(MONGO_DB_URL)) as mockMongoClient:
        mockMongoClient.get_database()[Lists.TODO_LIST_NAME].insert_many(todos_json)

        # When
        response = client.get('/')

        # Then
        assert b"Valid Item" in response.data
        assert b"Some other Item" in response.data
        assert b"An Item with a due" in response.data
        assert b"Sep 22" in response.data


def test_add_item_with_a_todo(client):
    with patch.object(mongo_database.MongoDatabase, "client", mongomock.MongoClient(MONGO_DB_URL)) as mockMongoClient:
        # Given
        todo_collection = mockMongoClient.get_database()[Lists.TODO_LIST_NAME]

        form_data = {
            "newitem": "Valid Item",
            "duedate": "2020-10-21"
        }

        # When
        client.post('/additem', data=form_data)

        # Then
        stored_obj = todo_collection.find({'title': 'Valid Item'}).next()
        assert {'title': 'Valid Item', 'duedate': '2020-10-21', 'status':'Not Started'}.items() <= stored_obj.items()
