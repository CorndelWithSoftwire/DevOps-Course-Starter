import app, Trello_items, pytest

TEST_LIST1 = [
    Trello_items.Item('1','ITEM1','Doing'), 
    Trello_items.Item('2','ITEM2','Completed'),
    Trello_items.Item('3','ITEM3','To Do'),
    Trello_items.Item('4','ITEM4','To Do'),
    Trello_items.Item('5','ITEM5','Completed'),
    Trello_items.Item('6','ITEM6','To Do'),
    Trello_items.Item('7','ITEM7','Doing')
    ]
TEST_LIST2 = [
    Trello_items.Item('1','ITEM1','To Do'), 
    Trello_items.Item('2','ITEM2','To Do'),
    Trello_items.Item('3','ITEM3','To Do'),
    Trello_items.Item('4','ITEM4','To Do'),
    Trello_items.Item('5','ITEM5','To Do'),
    Trello_items.Item('6','ITEM6','To Do'),
    Trello_items.Item('7','ITEM7','To Do')
    ]
TEST_LIST3 = [
    Trello_items.Item('1','ITEM1','Doing'), 
    Trello_items.Item('2','ITEM2','Doing'),
    Trello_items.Item('3','ITEM3','Doing'),
    Trello_items.Item('4','ITEM4','Doing'),
    Trello_items.Item('5','ITEM5','Doing'),
    Trello_items.Item('6','ITEM6','Doing'),
    Trello_items.Item('7','ITEM7','Doing')
    ]
TEST_LIST4 = [
    Trello_items.Item('1','ITEM1','Completed'), 
    Trello_items.Item('2','ITEM2','Completed'),
    Trello_items.Item('3','ITEM3','Completed'),
    Trello_items.Item('4','ITEM4','Completed'),
    Trello_items.Item('5','ITEM5','Completed'),
    Trello_items.Item('6','ITEM6','Completed'),
    Trello_items.Item('7','ITEM7','Completed')
    ]
TEST_LIST5 = [
    Trello_items.Item('1','ITEM1','Doing'), 
    Trello_items.Item('7','ITEM7','Completed'),
    Trello_items.Item('5','ITEM5','Completed'),
    ]
TEST_LIST6 = [
    ]
TEST_LISTS = [TEST_LIST1, TEST_LIST2, TEST_LIST3, TEST_LIST4, TEST_LIST5, TEST_LIST6]
TEST_LISTS_WITH_NUMBER_OF_TODO_ITEMS = [(TEST_LIST1,3), (TEST_LIST2, 7), (TEST_LIST3,0), (TEST_LIST4,0), (TEST_LIST5,0), (TEST_LIST6,0)]

@pytest.mark.parametrize("TEST_ITEMS", TEST_LISTS)
def test_view_todoitems_contains_only_todo_items(TEST_ITEMS):
    view = app.ViewModel(TEST_ITEMS)
    for item in view.todoitems:
        assert item.status == "To Do"

@pytest.mark.parametrize("TEST_ITEMS, todo_number", TEST_LISTS_WITH_NUMBER_OF_TODO_ITEMS)
def test_view_todoitems_contains_correct_number_of_items(TEST_ITEMS, todo_number):
    view = app.ViewModel(TEST_ITEMS)   
    assert len(view.todoitems) == todo_number