from item import Item, Status
from viewmodel import ViewModel

not_started = [
    Item(item_id=1, tittle="todo 1", desc='todo 1', status=Status.NOT_STARTED),
    Item(item_id=1, tittle="todo 2", desc='todo 2', status=Status.NOT_STARTED)
]
completed = [
    Item(item_id=1, tittle="completed 1", desc='completed 1', status=Status.COMPLETED),
    Item(item_id=1, tittle="completed 2", desc='completed 2', status=Status.COMPLETED)
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
