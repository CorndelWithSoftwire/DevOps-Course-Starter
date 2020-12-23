from datetime import date, timedelta

from todo_app.item import Item, Status
from todo_app.viewmodel import ViewModel

not_started = [
    Item(item_id=1, tittle="todo 1", desc='todo 1', status=Status.NOT_STARTED),
    Item(item_id=1, tittle="todo 2", desc='todo 2', status=Status.NOT_STARTED)
]
completed = [
    Item(item_id=1, tittle="completed 1", desc='completed 1', status=Status.COMPLETED),
    Item(item_id=1, tittle="completed 2", desc='completed 2', status=Status.COMPLETED,
         last_changed=date.today() - timedelta(days=1))
]
items = not_started + completed

view_model = ViewModel(items)


def test_items():
    assert items == view_model.items


def test_todo_items():
    todo_items = view_model.todo_items
    assert not_started == todo_items


def test_done_items():
    done_items = view_model.done_items
    assert completed == done_items


def test_recent_done_items():
    recent_done_items = view_model.recent_done_items
    assert completed[:1] == recent_done_items


def test_older_done_items():
    older_done_items = view_model.older_done_items
    assert completed[1:] == older_done_items

