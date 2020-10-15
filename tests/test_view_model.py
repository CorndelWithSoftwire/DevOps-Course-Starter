def test_view_model_can_show_todo_items():
  # Setup
  items = [
    ViewModel(1, "To Do", "A new todo"),
    ViewModel(2, "Done", "A done todo")
  ]
  # Act
  view_model = ViewModel(items)
  todo_items = view_model.todo_items # Note we're using the property here
  # Assert
  assert len(todo_items) == 1
  assert todo_items[0].status == "To Do"