import pytest
import os
from todo_app import create_app


@pytest.fixture(autouse=True)
def client():
    app = create_app("TEST")

    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
