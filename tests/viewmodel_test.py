from todo_app.view_model import ViewModel
from todo_app.data.todo_item import TodoItem

def test_view_model_can_show_todo_items():
    items = [
        TodoItem("1", "To Do", "New Todo"),
        TodoItem("2", "Doing", "New Doing"),
        TodoItem("3", "Done", "New Done")
    ]

    view_model = ViewModel(items, todo, doing, done)

    todo_items = view_model.todo
    doing_items = view_model.doing
    done_items = view_model.done

    assert len(todo_items) == 1

    todo_item = todo_items[0]

    assert todo_item.title == "New Todo"
    assert todo_item.status == "To Do"
    assert todo_item.id == "1"

# show all the completed items, or just the most recent ones.

    def test_show_all_done_items():
        pass

# return all the tasks that have been completed today.

    def test_recent_done_items():
        pass

# Return all of the tasks that were completed before today.

    def test_older_done_items():
        pass