import pytest
from todo_app.view_model import ViewModel
from datetime import datetime, timedelta
import os 
from todo_app.todo_item import TodoItem
from dotenv import load_dotenv, find_dotenv


@pytest.fixture
def view_model():
    file_path = find_dotenv(".env.test")
    load_dotenv(file_path, override=True)
    _DEFAULT_CARDS = [
        {
            "idShort": 1,
            "idList": os.getenv("to_do_list"),
            "name": "List saved todo items",
            "dateLastActivity": '2021-06-18T11:27:41.098Z',
            "due": '2030-06-18T11:27:41.098Z'
        },
        {
            "idShort": 2,
            "idList": os.getenv("in_progress_list"),
            "name": "List in progress items",
            "dateLastActivity": '2021-06-18T11:27:41.098Z',
            "due": '2030-06-18T11:27:41.098Z'
        },
        {
            "idShort": 3,
            "idList": os.getenv("complete_list"),
            "name": "List completed items",
            "dateLastActivity": '2000-06-18T11:27:41.098Z',
            "due": '2030-06-18T11:27:41.098Z'
        },
        {
            "idShort": 4,
            "idList": os.getenv("complete_list"),
            "name": "List completed items",
            "dateLastActivity": '2023-06-18T11:27:41.098Z',
            "due": '2030-06-18T11:27:41.098Z'
        },
    ]

    items=[]
    for card in _DEFAULT_CARDS:
        items.append(TodoItem(card))
    view_model = ViewModel(items)
    return view_model


def test_items(view_model):
    assert type(view_model.items) == list


def test_todo_items(view_model):
    assert len(view_model.todo_items) == 1
    for item in view_model.todo_items:
        assert item.status == "To Do"

def test_in_progress_items(view_model):
    if len(view_model.in_progress_items) >= 1:
        for item in view_model.in_progress_items:
            assert item.status == "In Progress"
    else: 
        assert view_model.in_progress_items == []


def test_complete_items(view_model):
    if len(view_model.complete_items) >= 1:
        for item in view_model.complete_items:
            assert item.status == "Complete"
    else: 
        assert view_model.complete_items == []


def test_show_all_done_items(view_model):
    assert len(view_model.complete_items) <= 5


def test_recent_done_items(view_model):
    datetime_yesterday = datetime.now() - timedelta(days=1)
    for item in view_model.recent_done_items:
        assert (item.status == "Complete") and (
            item.last_edited > datetime_yesterday
        )


def test_older_done_items(view_model):
    datetime_yesterday = datetime.now() - timedelta(days=1)
    for item in view_model.older_done_items:
        assert (item.status == "Complete") and (
            item.last_edited < datetime_yesterday
        )
