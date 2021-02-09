from items_view_model import ItemsViewModel
from item import Item
from datetime import datetime, date, timedelta

def test_can_get_todo_items_only():
    items = [
        Item("1", "Todo item", datetime.now(), "Things To Do"),
        Item("2", "Doing item", datetime.now(), "Doing"),
        Item("3", "Done item", datetime.now(), "Done"),
    ]

    view_model = ItemsViewModel(items)

    todo_items = view_model.todo_items

    assert len(todo_items) == 1

    todo_item = todo_items[0]

    assert todo_item.status == "Things To Do"
    assert todo_item.title == "Todo item"
    assert todo_item.id == "1"


def test_can_get_doing_items_only():
    items = [
        Item("1", "Todo item", datetime.now(), "Things To Do"),
        Item("2", "Doing item", datetime.now(), "Doing"),
        Item("3", "Done item", datetime.now(), "Done"),
    ]

    view_model = ItemsViewModel(items)

    todo_items = view_model.doing_items

    assert len(todo_items) == 1

    todo_item = todo_items[0]

    assert todo_item.status == "Doing"
    assert todo_item.title == "Doing item"
    assert todo_item.id == "2"


def test_can_get_done_items_only():
    items = [
        Item("1", "Todo item", datetime.now(), "Things To Do"),
        Item("2", "Doing item", datetime.now(), "Doing"),
        Item("3", "Done item", datetime.now(), "Done"),
    ]

    view_model = ItemsViewModel(items)

    todo_items = view_model.done_items

    assert len(todo_items) == 1

    todo_item = todo_items[0]

    assert todo_item.status == "Done"
    assert todo_item.title == "Done item"
    assert todo_item.id == "3"

def test_show_all_items_when_less_than_five():
    items = [
        Item("3", "Done item", datetime.now(), "Done"),
        Item("3", "Done item", datetime.now(), "Done"),
        Item("3", "Done item", datetime.now(), "Done"),
        Item("3", "Done item", datetime.now(), "Done"),
    ]

    view_model = ItemsViewModel(items)

    assert view_model.show_all_done_items == True


def test_show_all_items_when_five_or_more():
    items = [
        Item("3", "Done item", datetime.now(), "Done"),
        Item("3", "Done item", datetime.now(), "Done"),
        Item("3", "Done item", datetime.now(), "Done"),
        Item("3", "Done item", datetime.now(), "Done"),
        Item("3", "Done item", datetime.now(), "Done"),
    ]

    view_model = ItemsViewModel(items)

    assert view_model.show_all_done_items == False


def test_show_recent_items():
    today = date.today()
    today_datetime = datetime(
        year=today.year, 
        month=today.month,
        day=today.day,
    )

    yesterday = today - timedelta(days=1)
    yesterday_datetime = datetime(
        year=yesterday.year, 
        month=yesterday.month,
        day=yesterday.day,
    )


    items = [
        Item("3", "New Done item", today_datetime, "Done"),
        Item("3", "Older Done item", yesterday_datetime, "Done"),
    ]

    view_model = ItemsViewModel(items)

    assert len(view_model.recent_done_items) == 1

    recent_done_item = view_model.recent_done_items[0]

    assert recent_done_item.title == "New Done item"

def test_show_old_items():
    today = date.today()
    today_datetime = datetime(
        year=today.year, 
        month=today.month,
        day=today.day,
    )

    yesterday = today - timedelta(days=1)
    yesterday_datetime = datetime(
        year=yesterday.year, 
        month=yesterday.month,
        day=yesterday.day,
    )


    items = [
        Item("3", "New Done item", today_datetime, "Done"),
        Item("3", "Older Done item", yesterday_datetime, "Done"),
    ]

    view_model = ItemsViewModel(items)

    assert len(view_model.recent_done_items) == 1

    recent_done_item = view_model.older_done_items[0]

    assert recent_done_item.title == "Older Done item"