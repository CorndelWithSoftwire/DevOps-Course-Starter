import pytest
import app
from dotenv import load_dotenv, find_dotenv
from unittest.mock import patch, Mock


sample_trello_cards_response = [{
    'id':123,
    'name': 'something'
}]

query = {
    'Key':'1234abcd7b396482a18647f3aadd836',
    'Token':'12340e398b251cc85c1d9699203b65e33b8b84430b219643c6ec510412848c6c'
}

Board_ID='123ab456c07d891efgh2ij34'

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


@patch("requests.get")
def test_index_page(mock_get_requests, client):
    # Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect = mock_get_cards
    response = client.get("/")


def mock_get_cards(get_cards_url, params):
    if get_cards_url == f"https://api.trello.com/1/boards/{Board_ID}/cards":
        response = Mock()

    # sample_trello_lists_response should point to some test response data
        response.json.return_value = sample_trello_cards_response
        return response

    return None

# print(mock_get_cards("https://api.trello.com/1/boards/123ab456c07d891efgh2ij34/cards", params=query))

if __name__ =='__main__':
    unittest.mock()
