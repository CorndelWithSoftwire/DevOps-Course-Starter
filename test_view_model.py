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

    