import pytest
from todo_app.data.item import Item
from todo_app.viewmodel import ViewModel

@pytest.fixture
def generateItems():
  item1 = Item('1', "To Do", "A new todo", 'xx')
  item2 = Item('2', "Done", "A done todo", 'yy')
  items = [ item1, item2 ]
  return items
    
def test_view_model_can_show_all_items(generateItems):
  # Setup via fixture

  # Act
  view_model = ViewModel(generateItems)
  todo_items = view_model.todo_items 
  
  # Assert
  assert len(todo_items) == 2


def test_view_model_can_show_todo_items(generateItems):
  # Setup via fixture

  # Act
  view_model = ViewModel(generateItems)
  todo_items = view_model.todo_items 
  
  # Assert
  assert len(todo_items) == 1
  assert todo_items[0].status == "To Do"