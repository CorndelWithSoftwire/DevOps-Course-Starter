import app, Trello_items, pytest

TEST_LIST1 = [
    Trello_items.Item('1','ITEM1','Doing'), 
    Trello_items.Item('2','ITEM2','Done'),
    Trello_items.Item('3','ITEM3','To Do'),
    Trello_items.Item('4','ITEM4','To Do'),
    Trello_items.Item('5','ITEM5','Done'),
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
    Trello_items.Item('1','ITEM1','Done'), 
    Trello_items.Item('2','ITEM2','Done'),
    Trello_items.Item('3','ITEM3','Done'),
    Trello_items.Item('4','ITEM4','Done'),
    Trello_items.Item('5','ITEM5','Done'),
    Trello_items.Item('6','ITEM6','Done'),
    Trello_items.Item('7','ITEM7','Done')
    ]
TEST_LIST5 = [
    Trello_items.Item('1','ITEM1','Doing'), 
    Trello_items.Item('7','ITEM7','Done'),
    Trello_items.Item('5','ITEM5','Done'),
    ]
TEST_LIST6 = [
    ]
TEST_LISTS = [TEST_LIST1, TEST_LIST2, TEST_LIST3, TEST_LIST4, TEST_LIST5, TEST_LIST6]
TEST_LISTS_WITH_NUMBER_OF_TODO_ITEMS = [(TEST_LIST1,3), (TEST_LIST2, 7), (TEST_LIST3,0), (TEST_LIST4,0), (TEST_LIST5,0), (TEST_LIST6,0)]
TEST_LISTS_WITH_NUMBER_OF_DOING_ITEMS = [(TEST_LIST1,2), (TEST_LIST2, 0), (TEST_LIST3,7), (TEST_LIST4,0), (TEST_LIST5,1), (TEST_LIST6,0)]
TEST_LISTS_WITH_NUMBER_OF_DONE_ITEMS = [(TEST_LIST1,2), (TEST_LIST2, 0), (TEST_LIST3,0), (TEST_LIST4,7), (TEST_LIST5,2), (TEST_LIST6,0)]

@pytest.mark.parametrize("TEST_ITEMS", TEST_LISTS)
def test_view_todoitems_contains_only_todo_items(TEST_ITEMS):
    view = app.ViewModel(TEST_ITEMS)
    for item in view.todoitems:
        assert item.status == "To Do"

@pytest.mark.parametrize("TEST_ITEMS, number_of_todo_items", TEST_LISTS_WITH_NUMBER_OF_TODO_ITEMS)
def test_view_todoitems_contains_correct_number_of_items(TEST_ITEMS, number_of_todo_items):
    view = app.ViewModel(TEST_ITEMS)   
    assert len(view.todoitems) == number_of_todo_items

@pytest.mark.parametrize("TEST_ITEMS", TEST_LISTS)
def test_view_doingitems_contains_only_doing_items(TEST_ITEMS):
    view = app.ViewModel(TEST_ITEMS)
    for item in view.doingitems:
        assert item.status == "Doing"

@pytest.mark.parametrize("TEST_ITEMS, number_of_doing_items", TEST_LISTS_WITH_NUMBER_OF_DOING_ITEMS)
def test_view_doingitems_contains_correct_number_of_items(TEST_ITEMS, number_of_doing_items):
    view = app.ViewModel(TEST_ITEMS)   
    assert len(view.doingitems) == number_of_doing_items

@pytest.mark.parametrize("TEST_ITEMS", TEST_LISTS)
def test_view_show_all_done_items_contains_only_done_items(TEST_ITEMS):
    view = app.ViewModel(TEST_ITEMS)
    for item in view.show_all_done_items:
        assert item.status == "Done"

@pytest.mark.parametrize("TEST_ITEMS, number_of_done_items", TEST_LISTS_WITH_NUMBER_OF_DONE_ITEMS)
def test_view_show_all_done_items_contains_correct_number_of_items(TEST_ITEMS, number_of_done_items):
    view = app.ViewModel(TEST_ITEMS)   
    assert len(view.show_all_done_items) == number_of_done_items

