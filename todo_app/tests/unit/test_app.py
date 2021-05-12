import pytest
from datetime import datetime
from todo_app.viewModel import ViewModel
from todo_app.data.item import Item

def test_app():
    viewModel =ViewModel([])
    assert len(viewModel.items) == 0


def test_todoitems():
    item1 = Item(1, "Title 1", "ToDo")
    item2 = Item(1, "Title 2", "ToDo")
    item3 = Item(1, "Title 3", "ToDo")
    item4 = Item(1, "Title 4", "ToDo")
    items = [item1, item2, item3, item4 ]
    viewModel =ViewModel(items)
    
    assert len(viewModel.todoitems) == 4
 