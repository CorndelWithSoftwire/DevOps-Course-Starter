from todo_app.view_model import ViewModel
from todo_app.data.todo_item import TodoItem

def test_view_model_can_show_todo_items():
    items = [
        TodoItem("1", "To Do", "New Todo"),
        TodoItem("2", "Done", "Done Todo")
    ]

    view_model = ViewModel(items)

    todo_items = view_model.todo

    assert len(todo_items) == 1

    todo_item = todo_items[0]

    assert todo_item.title == "New Todo"
    assert todo_item.status == "To Do"
    assert todo_item.id == "1"