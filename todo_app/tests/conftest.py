
from os import environ, path
from dotenv import load_dotenv
import pytest

#Tip: We can load in environment variables
# from our .env file using
# the load_dotenv function from
# the dotenv package.

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be  used in our tests.
    with test_app.test_client() as client:
        yield client


# def test_get_root(test_client):
#     response = test_client.get('/')
#     assert response.status_code == 200


# Check a GET request to root path works   
    # additional response checks go here