from datetime import datetime, timedelta
from unittest import TestCase

from todoapp.common import NOT_STARTED, TodoItem, COMPLETED
from todoapp.viewmodel import ViewModel


class TestViewModel(TestCase):
    def test_todo_items(self):
        # Arrange
        todoItem = TodoItem("this is a todo item", NOT_STARTED, 1)
        doneItem = TodoItem("this is a done item", COMPLETED, 2)
        items = [todoItem, doneItem]
        viewModel = ViewModel(items)

        # Act
        todoItems = viewModel.todo

        # Assert
        assert len(todoItems) == 1 and todoItems[0] == todoItem

    def test_done_items(self):
        # Arrange
        todoItem = TodoItem("this is a todo item", NOT_STARTED, 1)
        doneItem = TodoItem("this is a done item", COMPLETED, 2)
        items = [todoItem, doneItem]
        viewModel = ViewModel(items)

        # Act
        doneItems = viewModel.done

        # Assert
        assert len(doneItems) == 1 and doneItems[0] == doneItem

    def test_show_all_done_if_less_than_five_items(self):
        # Arrange
        todoItem = TodoItem("this is a todo item", NOT_STARTED, 1)
        doneItem1 = TodoItem("this is a done item", COMPLETED, 2)
        doneItem2 = TodoItem("this is a done item", COMPLETED, 2)
        doneItem3 = TodoItem("this is a done item", COMPLETED, 2)
        items = [todoItem, doneItem1, doneItem2, doneItem3]
        viewModel = ViewModel(items)

        # Act
        show_all_done = viewModel.show_all_done_items

        # Assert
        assert show_all_done

    def test_show_all_done_items_is_false_if_great_than_or_equal_to_five_items(self):
        # Arrange
        todoItem = TodoItem("this is a todo item", NOT_STARTED, 1)
        doneItem1 = TodoItem("this is a done item", COMPLETED, 2)
        doneItem2 = TodoItem("this is a done item", COMPLETED, 2)
        doneItem3 = TodoItem("this is a done item", COMPLETED, 2)
        doneItem4 = TodoItem("this is a done item", COMPLETED, 2)
        doneItem5 = TodoItem("this is a done item", COMPLETED, 2)
        items = [todoItem, doneItem1, doneItem2, doneItem3, doneItem4, doneItem5]
        viewModel = ViewModel(items)

        # Act
        show_all_done = viewModel.show_all_done_items

        # Assert
        assert not show_all_done

    def test_recent_done_items_return_all_today(self):
        # Arrange
        todoItem = TodoItem("this is a todo item", NOT_STARTED, 1)
        doneItem1 = TodoItem("this is a done item", COMPLETED, 2, last_modified=datetime.now().isoformat())
        doneItem2 = TodoItem("this is a done item", COMPLETED, 2, last_modified=datetime.now().isoformat())
        doneItem3 = TodoItem("this is a done item", COMPLETED, 2, last_modified=datetime.now().isoformat())
        doneItem4 = TodoItem("this is a done item", COMPLETED, 2, last_modified=(datetime.now() - timedelta(days=1)).isoformat())
        doneItem5 = TodoItem("this is a done item", COMPLETED, 2, last_modified=(datetime.now() - timedelta(days=1)).isoformat())
        items = [todoItem, doneItem1, doneItem2, doneItem3, doneItem4, doneItem5]
        viewModel = ViewModel(items)

        # Act
        recent_done_items = viewModel.recent_done_items

        # Assert
        assert len(recent_done_items) == 3 and recent_done_items == [doneItem1, doneItem2, doneItem3]

    def test_older_done_items_return_all_today(self):
        # Arrange
        todoItem = TodoItem("this is a todo item", NOT_STARTED, 1)
        doneItem1 = TodoItem("this is a done item", COMPLETED, 2, last_modified=datetime.now().isoformat())
        doneItem2 = TodoItem("this is a done item", COMPLETED, 2, last_modified=datetime.now().isoformat())
        doneItem3 = TodoItem("this is a done item", COMPLETED, 2, last_modified=datetime.now().isoformat())
        doneItem4 = TodoItem("this is a done item", COMPLETED, 2, last_modified=(datetime.now() - timedelta(days=1)).isoformat())
        doneItem5 = TodoItem("this is a done item", COMPLETED, 2, last_modified=(datetime.now() - timedelta(days=1)).isoformat())
        items = [todoItem, doneItem1, doneItem2, doneItem3, doneItem4, doneItem5]
        viewModel = ViewModel(items)

        # Act
        older_done_items = viewModel.older_done_items

        # Assert
        assert len(older_done_items) == 2 and older_done_items == [doneItem4, doneItem5]
