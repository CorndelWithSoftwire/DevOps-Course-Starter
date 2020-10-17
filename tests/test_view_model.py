import pytest
from todo_app.data.item import Item
from todo_app.viewmodel import ViewModel
import iso8601

@pytest.fixture
def generateItems():
  date1 = iso8601.parse_date('2020-10-16T13:42:52.101Z')
  date2 = iso8601.parse_date('2020-10-15T13:42:52.101Z')
  date3 = iso8601.parse_date('2020-10-16T13:42:52.101Z')
  date4 = iso8601.parse_date('2020-10-15T13:42:52.101Z')
  date5 = iso8601.parse_date('2020-10-15T13:42:52.101Z')
  date6 = iso8601.parse_date('2020-10-16T13:42:52.101Z')
  date7 = iso8601.parse_date('2020-10-16T13:42:52.101Z')
  date8 = iso8601.parse_date('2020-10-16T13:42:52.101Z')

  item1 = Item('1', "To Do", "A new todo", 'xx', date1)
  item2 = Item('2', "Done", "A done todo", 'yy', date2)
  item3 = Item('3', "Doing", "In progress todo", 'yy', date3 )
  item4 = Item('4', "Done", "Completed todo", 'yy', date4)
  item5 = Item('5', "Done", "Completed todo", 'yy', date5)
  item6 = Item('6', "Done", "Completed todo", 'yy', date6)
  item7 = Item('7', "Done", "Completed todo", 'yy', date7)
  item8 = Item('8', "Done", "Completed todo", 'yy', date8)
  items = [ item1, item2, item3, item4, item5, item6, item7, item8 ]
  return items
    
def test_view_model_can_show_all_items(generateItems):
  # Setup via fixture

  # Act
  view_model = ViewModel(generateItems)
  items = view_model.all_items 
  
  # Assert
  assert len(items) == 8


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
  assert len(done_items) == 6
  assert done_items[0].status == "Done"

def test_view_model_can_show_done_items_all(generateItems):
  # Setup via fixture

  # Act
  view_model = ViewModel(generateItems)
  done_items = view_model.show_all_done_items 
  
  # Assert
  assert len(done_items) == 5
  assert done_items[0].status == "Done"

def test_view_model_can_recent_done_items(generateItems):
  # Setup via fixture

  # Act
  view_model = ViewModel(generateItems)
  done_items = view_model.recent_done_items 
  
  # Assert
  assert len(done_items) == 0

def test_view_model_can_past_done_items(generateItems):
  # Setup via fixture

  # Act
  view_model = ViewModel(generateItems)
  done_items = view_model.older_done_items
  
  # Assert
  assert len(done_items) > 0