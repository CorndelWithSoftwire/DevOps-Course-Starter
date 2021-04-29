from datetime import datetime

import mongomock
import pymongo
import pytest
from bson import ObjectId
from dotenv import find_dotenv, load_dotenv

from todo_app import app
from todo_app.item import Status


@pytest.fixture
def client():
    with mongomock.patch(servers=('mongodb://example:27017/',)):
        # Use our test integration config instead of the 'real' version
        file_path = find_dotenv('../.env.test')
        load_dotenv(file_path, override=True)
        # Create the new app.
        test_app = app.create_app()
        # Use the app to create a test_client that can be used in our tests.
        with test_app.test_client() as client:
            yield client


def test_index_page(client):
    docs = [{'_id': ObjectId(), 'name': 'test', 'status': Status.NOT_STARTED.name, 'desc': 'test', 'dateLastActivity': datetime.now()}]

    monngoclient = pymongo.MongoClient('mongodb://example:27017/')
    monngoclient.tododb.todo.insert_many(docs)

    response = client.get('/')
    assert response.status_code == 200
    assert 'test' in str(response.data)
