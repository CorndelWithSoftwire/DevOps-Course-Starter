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


def test_doingitems():
    item1 = Item(1, "Title 1","Doing")
    item2 = Item(1, "Title 2", "Doing")
    item3 = Item(1, "Title 3", "Doing")
    item4 = Item(1, "Title 4", "Doing")
    items = [item1, item2, item3, item4 ]
    viewModel =ViewModel(items)
    
    assert len(viewModel.doingitems) == 4
 
def test_doneitems():
    item1 = Item(1, "Title 1", "Done")
    item2 = Item(1, "Title 2", "Done")
    item3 = Item(1, "Title 3", "Done")
    item4 = Item(1, "Title 4", "Done")
    items = [item1, item2, item3, item4 ]
    viewModel =ViewModel(items)
    
    assert len(viewModel.doneitems) == 4
 