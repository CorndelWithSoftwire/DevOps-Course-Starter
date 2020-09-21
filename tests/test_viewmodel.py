from unittest import TestCase

from common import NOT_STARTED, TodoItem, COMPLETED
from viewmodel import ViewModel


class TestViewModel(TestCase):
    def test_todo_items(self):
        # Arrange
        todoItem = TodoItem("this is a todo item", NOT_STARTED, 1)
        doneItem = TodoItem("this is a done item", COMPLETED, 2)
        items = [todoItem, doneItem]
        viewModel = ViewModel(items)

        # Act
        todoItems = viewModel.todo

        #Assert
        assert len(todoItems) == 1 and todoItems[0] == todoItem

    def test_done_items(self):
        # Arrange
        todoItem = TodoItem("this is a todo item", NOT_STARTED, 1)
        doneItem = TodoItem("this is a done item", COMPLETED, 2)
        items = [todoItem, doneItem]
        viewModel = ViewModel(items)

        # Act
        doneItems = viewModel.done

        #Assert
        assert len(doneItems) == 1 and doneItems[0] == doneItem
