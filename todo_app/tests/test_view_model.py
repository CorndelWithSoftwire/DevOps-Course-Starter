import pytest
from view_model import ViewModel
from datetime import datetime, timedelta
from todo_item import TodoItem
import os
from dotenv import load_dotenv, find_dotenv


@pytest.fixture
def view_model():
    file_path = find_dotenv(".env.test")
    load_dotenv(file_path, override=True)

    _DEFAULT_ITEMS = [
        {
            "idShort": 1,
            "idList": os.getenv("LIST_ID_NOT_STARTED"),
            "name": "To-Do items",
            "dateLastActivity": "2021-04-21T09:59:06.065Z",
        },
        {
            "idShort": 2,
            "idList": os.getenv("LIST_ID_IN_PROGRESS"),
            "name": "In Progress Items",
            "dateLastActivity": "2021-04-21T09:59:06.065Z",
        },
        {
            "idShort": 3,
            "idList": os.getenv("LIST_ID_DONE"),
            "name": "Recent Done Items",
            "dateLastActivity": "3000-04-21T09:59:06.065Z",
        },
        {
            "idShort": 4,
            "idList": os.getenv("LIST_ID_DONE"),
            "name": "Older Done Items",
            "dateLastActivity": "2000-04-21T09:59:06.065Z",
        },
    ]
    items = []
    for item in _DEFAULT_ITEMS:
        items.append(TodoItem(item))

    view_model = ViewModel(items)

    return view_model


def test_items(view_model):
    assert type(view_model.items) == list


def test_todo_items(view_model):
    assert len(view_model.todo_items) == 1
    for item in view_model.todo_items:
        assert item.status == "To Do"


def test_doing_items(view_model):
    if len(view_model.doing_items) >= 1:
        for item in view_model.doing_items:
            assert item.status == "In Progress"
    else:
        assert view_model.doing_items == []


def test_done_items(view_model):
    if len(view_model.done_items) >= 1:
        for item in view_model.done_items:
            assert item.status == "Done"
    else:
        assert view_model.done_items == []


def test_show_all_done_items(view_model):
    assert len(view_model.done_items) <= 5


def test_recent_done_items(view_model):
    datetime_yesterday = datetime.now() - timedelta(days=1)
    for item in view_model.recent_done_items:
        assert (item.status == "Done") and (item.last_edited > datetime_yesterday)


def test_older_done_items(view_model):
    datetime_yesterday = datetime.now() - timedelta(days=1)
    for item in view_model.older_done_items:
        assert (item.status == "Done") and (item.last_edited < datetime_yesterday)
