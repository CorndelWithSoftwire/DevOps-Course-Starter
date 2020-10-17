import os
from dotenv import load_dotenv, find_dotenv
import flask
import requests
import responses
import requests_mock
import pytest
from unittest.mock import patch
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

    
@patch('app.bp.index')
#@patch('trello_app.index')
def test_index_page(mock_index, client):
    mock_index = mock_index.index().return_value={'id': '5f5a4c01846bb381f6f3fa8b', 'status': 'To Do', 'title': 'To Do 111', 'date': '2020-10-11'}
    response = client.get('/')
    assert response == mock_index