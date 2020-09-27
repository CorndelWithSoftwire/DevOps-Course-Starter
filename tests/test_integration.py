import pytest
from dotenv import find_dotenv, load_dotenv

import app
from flask_config import Config


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


def test_index_page(requests_mock, client):
    todoresp = [{'id': '1', 'name': 'test', 'idList': '1', 'desc': 'test', 'dateLastActivity': '2020-09-04T12:38:58.290Z'}]
    requests_mock.get(f'https://api.trello.com/1/lists/{Config.LIST_ID}/cards?key={Config.KEY}&token={Config.TOKEN}',
                      json=todoresp)
    doneresp = [{'id': '2', 'name': 'test', 'idList': '2', 'desc': 'test', 'dateLastActivity': '2020-09-04T12:38:58.290Z'}]
    requests_mock.get(
        f'https://api.trello.com/1/lists/{Config.DONE_LIST_ID}/cards?key={Config.KEY}&token={Config.TOKEN}', json=doneresp)
    response = client.get('/')
    assert response.status_code == 200
    assert 'test' in str(response.data)
