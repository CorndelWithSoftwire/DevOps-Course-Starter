from todo_app.data.item import Item
from todo_app.viewmodel import ViewModel


def test_view_model_can_show_todo_items():
  # Setup
  item1 = Item('1', "To Do", "A new todo", 'xx')
  item2 = Item('2', "Done", "A done todo", 'yy')
  items = [
    item1,
    item2
  ]
  # Act
  view_model = ViewModel(items)
  todo_items = view_model.todo_items 
  
  # Assert
  assert len(todo_items) == 2
  assert todo_items[0].status == "To Do"