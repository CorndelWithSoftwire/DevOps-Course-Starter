import os
from dotenv import load_dotenv, find_dotenv
import flask
import json
import requests
import responses
import requests_mock
import pytest
from unittest.mock import patch, Mock
import unittest
from requests_mock_flask import add_flask_app_to_mock

import app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    test_app = app.create_app()
    with test_app.test_client() as client:
        yield client

    
#@patch('app.trello_bp.index')
@patch('requests.request')
#@patch('trello_app.index')
def test_index_page(mock_request, client):
    mock_request.side_effect = mock_test_req
    #mock_index = mock_index.index().return_value={'id': '5f5a4c01846bb381f6f3fa8b', 'status': 'To Do', 'title': 'To Do 111', 'date': '2020-10-11'}
    response = client.get('/')
    #assert response == mock_index
    assert response.status_code == 200
    assert 'To Do' in response.data.decode()
    assert 'To Do 111' in response.data.decode()


def mock_test_req(method, url, params):
    mock_test_resp = Mock()
    mock_test_resp.text = json.dumps([{'id': '5f5a4c01846bb381f6f3fa8b', 'idList': '5f5a4b008a129438843fcf10', 'name': 'To Do 111', 'dateLastActivity': '2020-10-11'}])
    return mock_test_resp
