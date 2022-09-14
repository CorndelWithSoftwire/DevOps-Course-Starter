from todo_app.data.get_items import ViewModel

from todo_app.data.item import Item

def test_todo_items_property_only_shows_todo_items_and_not_anything_else():
   
    #Arrange

    items = [
        Item("1", "A Test Todo", "To Do"),
        Item("2", "An in progress Todo", "Doing"),
        Item("3", "A completed Todo", "Done")
    ]

    get_items = ViewModel(items)
  
    #Act
    test_todo_items = get_items.todo_items


    #Assert

    assert len(test_todo_items) == 1

    todo_item = test_todo_items[0]

    assert todo_item.id == "1"
    assert todo_item.title == "A Test Todo"
    assert todo_item.status == "To Do"

def test_done_items_property_only_shows_done_items_and_not_anything_else():

    #Arrange

    items = [

        Item("1", "A Test Todo", "To Do"),
        Item("2", "An in progress Todo", "Doing"),
        Item("3", "A completed Todo", "Done")

    ]
    get_items = ViewModel(items)

    #Act

    test_done_items = get_items.done_items

    #Assert
    
    assert len(test_done_items) == 1

    done_item = test_done_items[0]

    assert done_item.id == "3"
    assert done_item.title == "A completed Todo"
    assert done_item.status == "Done"