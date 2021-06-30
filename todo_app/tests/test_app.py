import pytest
import app
from dotenv import load_dotenv, find_dotenv
import os
import requests


@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv(".env.test")
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client


def test_index_page(client, monkeypatch):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = f"https://api.trello.com/1/boards/{os.getenv('BOARD_ID')}/cards"

        def json(self):
            return [
                {
                    "idShort": "5678",
                    "idList": "f",
                    "name": "test",
                    "dateLastActivity": "2021-04-21T09:59:06.065Z",
                }
            ]

    def mock_get(url, params={}):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    response = client.get("/")
    assert "test" in response.data.decode("utf-8") and response.status_code == 200
