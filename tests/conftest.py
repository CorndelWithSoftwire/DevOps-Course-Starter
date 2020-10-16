from flask import config
import pytest
from todo_app import app as flask_app

@pytest.fixture
def app():
    flask_app.app.testing = True
    yield flask_app

@pytest.fixture
def client(app):
    return app.app.test_client()