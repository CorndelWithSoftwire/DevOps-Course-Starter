import pytest
from view_model import ViewModel
from datetime import datetime, timedelta
import pdb


@pytest.fixture
def view_model():
    _DEFAULT_ITEMS = [
        {
            "id": 1,
            "status": "To Do",
            "title": "List saved todo items",
            "last_edited": datetime(2021, 3, 31, 13, 46, 34, 58000),
        },
        {
            "id": 2,
            "status": "In Progress",
            "title": "List in progress items",
            "last_edited": datetime(2021, 3, 31, 13, 46, 34, 58000),
        },
        {
            "id": 3,
            "status": "Complete",
            "title": "List completed items",
            "last_edited": datetime(2000, 4, 10, 13, 46, 34, 58000),
        },
        {
            "id": 4,
            "status": "Complete",
            "title": "List completed items",
            "last_edited": datetime(2023, 4, 30, 13, 46, 34, 58000),
        },
    ]

    view_model = ViewModel(_DEFAULT_ITEMS)
    return view_model


def test_items(view_model):
    assert type(view_model.items) == list


def test_todo_items(view_model):
    for item in view_model.todo_items:
        assert item["status"] == "To Do"


def test_in_progress_items(view_model):
    for item in view_model.in_progress_items:
        assert item["status"] == "In Progress"


def test_complete_items(view_model):
    for item in view_model.complete_items:
        assert item["status"] == "Complete"


def test_show_all_done_items(view_model):
    assert len(view_model.complete_items) <= 5


def test_recent_done_items(view_model):
    datetime_yesterday = datetime.now() - timedelta(days=1)
    for item in view_model.recent_done_items:
        assert (item["status"] == "Complete") and (
            item["last_edited"] > datetime_yesterday
        )


def test_older_done_items(view_model):
    datetime_yesterday = datetime.now() - timedelta(days=1)
    for item in view_model.older_done_items:
        assert (item["status"] == "Complete") and (
            item["last_edited"] < datetime_yesterday
        )
