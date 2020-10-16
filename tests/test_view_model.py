import pytest
from todo_app.data.item import Item
from todo_app.viewmodel import ViewModel

@pytest.fixture
def generateItems():
  item1 = Item('1', "To Do", "A new todo", 'xx')
  item2 = Item('2', "Done", "A done todo", 'yy')
  item3 = Item('3', "Doing", "In progress todo", 'yy')
  item4 = Item('4', "Done", "Completed todo", 'yy')
  items = [ item1, item2, item3, item4 ]
  return items
    
def test_view_model_can_show_all_items(generateItems):
  # Setup via fixture

  # Act
  view_model = ViewModel(generateItems)
  items = view_model.all_items 
  
  # Assert
  assert len(items) == 4


def test_view_model_can_show_todo_items(generateItems):
  # Setup via fixture

  # Act
  view_model = ViewModel(generateItems)
  todo_items = view_model.todo_items 
  
  # Assert
  assert len(todo_items) == 1
  assert todo_items[0].status == "To Do"

def test_view_model_can_show_doing_items(generateItems):
  # Setup via fixture

  # Act
  view_model = ViewModel(generateItems)
  doing_items = view_model.doing_items 
  
  # Assert
  assert len(doing_items) == 1
  assert doing_items[0].status == "Doing"

def test_view_model_can_show_done_items(generateItems):
  # Setup via fixture

  # Act
  view_model = ViewModel(generateItems)
  done_items = view_model.done_items 
  
  # Assert
  assert len(done_items) == 2
  assert done_items[0].status == "Done"