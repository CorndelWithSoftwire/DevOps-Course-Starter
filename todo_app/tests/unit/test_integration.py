
# from unittest.mock import patch, Mock
# # Step 3: Patch the call to the Trello API
# # Let's start by testing our index endpoint. We can use the test client
# # to make a call to our main page.

# def test_index_page(client):
#     response = client.get('/')

# @patch('requests.get')
# def test_index_page(mock_get_requests, client):
# # Replace call to requests.get(url) with our own function
#     mock_get_requests.side_effect = mock_get_lists
#     response = client.get('/')

# def mock_get_lists(url, params):
#     if url == f'https://api.trello.com/1/boards/{TEST_BOARD_ID}/lists':
#         response = Mock()
#         # sample_trello_lists_response should point to some test response data
#         response.json.return_value = sample_trello_lists_response
#         return response
#     return None


