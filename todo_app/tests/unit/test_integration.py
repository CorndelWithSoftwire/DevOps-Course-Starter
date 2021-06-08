
from os import environ, path
from dotenv import load_dotenv, find_dotenv
from requests import status_codes
from todo_app import app
import pytest
from unittest.mock import patch, Mock
from todo_app.tests.unit.mockTrello_data import mock_get

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


#todo_app\tests\unit\mockTrello_data.py
@patch('requests.get')
def test_index_page(mock_get_requests, client):
# Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect =  mock_get_lists
    response = client.get('/')
    result = response.data.decode()
    assert sample_trello_lists_response()[0]['name'] in result

    
def mock_get_lists(url, params):
    if url == f'https://api.trello.com/1/boards/boardid/cards':
        response = Mock()
        # sample_trello_lists_response should pointto some test response data
        response.json.return_value =sample_trello_lists_response()
        #response.json.return_value = mock_get('GET', url)
        return response
    return None


def sample_trello_lists_response():
    data = [{"id":"6054b0789b71d43acb0d5581","checkItemStates":[],"closed":False,"dateLastActivity":"2021-05-18T16:15:47.200Z",
  "desc":"","descData":None,"dueReminder":None,"idBoard":"6054b0101e6a3d49645dbdc8","idList":"todolistid",
  "idMembersVoted":[],"idShort":1,"idAttachmentCover":None,"idLabels":[],"manualCoverAttachment":False,"name":"DevopsTrelloBoard",
  "pos":65535,"shortLink":"YFJtWyDm","isTemplate":False,"cardRole":None,"dueComplete":False,"due":None,"email":None,"labels":[],
  "shortUrl":"https://trello.com/c/YFJtWyDm","start":None,"url":"https://trello.com/c/YFJtWyDm/1-devopstrelloboard","idMembers":[],
  "badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":False,"votes":0,"viewingMemberVoted":False,
  "subscribed":False,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":None,"comments":0,"attachments":0,
  "description":False,"due":None,"dueComplete":False,"start":None},"subscribed":False,"idChecklists":[],
  "cover":{"idAttachment":None,"color":None,"idUploadedBackground":None,"size":"normal","brightness":"light","idPlugin":None}}]
    return data
    
   

@patch('requests.post')
def test_something_awesome(mocked_post):
    
    mocked_post.return_value = Mock(status_code=200, json=lambda : {"data": {"id":"6054b0101e6a3d49645dbdc9","name":"To Do","pos":16384,"idBoard":"6054b0101e6a3d49645dbdc8"}})


  
