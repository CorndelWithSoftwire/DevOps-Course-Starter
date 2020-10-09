from view_model import ViewModel
from card import Card

def test_todo_property():
    # Setup
    cards = [
        Card(1, "Todo Item", "", "Todo"),
        Card(2, "Done Item", "", "Done")
    ]

    view_model = ViewModel(cards)

    # Act
    todo_items = view_model.todo_items

    # Assert
    assert len(todo_items) == 1

    todo_item = todo_items[0]
    assert todo_item.status == "Todo"

def test_doing_property():
    cards = [
        Card(1, "Doing Item", "", "Doing"),
        Card(2, "Done Item", "", "Done")
    ]
    view_model = ViewModel(cards)

    doing_items = view_model.doing_items

    assert len(doing_items) == 1

    doing_item = doing_items[0]
    assert doing_item.status == "Doing"


def test_done_property():
    cards = [
        Card(2, "Done Item", "", "Done"),
        Card(1, "Doing Item", "", "Doing")
    ]
    view_model = ViewModel(cards)

    done_items = view_model.done_items

    assert len(done_items) == 1

    done_item = done_items[0]
    assert done_item.status == "Done"

    
