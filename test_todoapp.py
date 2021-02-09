import os
import tempfile
#import mock
import requests
import dotenv
import pytest
from flask import Flask, render_template, request, redirect, url_for, session
import trello_items as trello
import app as app
from threading import Thread 

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = dotenv.find_dotenv('.env.test')
    dotenv.load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

# @mock.patch('requests.get')
# def test_index_page(mock_get_requests, client):
#     response = client.get('/')

#     assert response.status_code == 302