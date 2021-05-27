import app, pytest, mongomock, os
import Mongo_items 
from mongo_config import Config
from dotenv import find_dotenv, load_dotenv

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

test_todos = [
    {
        "_id":"ObjectID(609e3da1407636a2a8b17a58)", 
        "title": "TestItem1", 
        "Lastmodifieddate" : "2021-05-13T09:06:41.902+00:00"},
    {
        "_id":"ObjectID(809e4da1408236a2a3f17a41)", 
        "title": "TestItem2", 
        "Lastmodifieddate" : "2021-05-11T12:06:41.902+00:00"
        },
    {
        "_id":"ObjectID(7641a11e48b88f47531a157)", 
        "title": "TestItem3", 
        "Lastmodifieddate" : "2021-05-21T15:16:41.857+00:00"
        },
    {
        "_id":"ObjectID(63547e9g987b23e4791b378)", 
        "title": "TestItem4", 
        "Lastmodifieddate" : "2021-05-17T09:24:04.654+00:00"
        }
    ]

def test_index(client, monkeypatch):
    def mock_get_db(*args):
        #mockdb = mongomock.MongoClient().fake_Mongo_db
        mockdb = mongomock.MongoClient().get_database(os.getenv("MONGO_DB"))
        mockdb.todo.insert_many(test_todos)
        return mockdb
   
    monkeypatch.setattr(Mongo_items, "get_db", mock_get_db)
   
    response = client.get('/')
    assert "TestItem1" in str(response.data)
    assert "TestItem2" in str(response.data)
    assert "TestItem3" in str(response.data)
    assert "TestItem4" in str(response.data)


