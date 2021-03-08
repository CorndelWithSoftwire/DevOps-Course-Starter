from dotenv import load_dotenv, find_dotenv

import pytest
from todo_app import app

@pytest.fixture(scope="module")
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Use our test integration config instead of the 'real' version
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

