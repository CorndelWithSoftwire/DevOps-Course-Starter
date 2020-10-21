import app, Trello_items, pytest, datetime

#list containing a mixture of items
TEST_LIST1 = [
    Trello_items.Item('1','ITEM1',datetime.date.today(),'Doing'), 
    Trello_items.Item('2','ITEM2',datetime.date.today(),'Done'),
    Trello_items.Item('3','ITEM3',datetime.date.today(),'To Do'),
    Trello_items.Item('4','ITEM4',datetime.date.today(),'To Do'),
    Trello_items.Item('5','ITEM5',datetime.date.today(),'Done'),
    Trello_items.Item('6','ITEM6',datetime.date.today(),'To Do'),
    Trello_items.Item('7','ITEM7',datetime.date.today(),'Doing')
    ]
#list containing only To Do items
TEST_LIST2 = [
    Trello_items.Item('1','ITEM1',datetime.date.today(),'To Do'), 
    Trello_items.Item('2','ITEM2',datetime.date.today(),'To Do'),
    Trello_items.Item('3','ITEM3',datetime.date.today(),'To Do'),
    Trello_items.Item('4','ITEM4',datetime.date.today(),'To Do'),
    Trello_items.Item('5','ITEM5',datetime.date.today(),'To Do'),
    Trello_items.Item('6','ITEM6',datetime.date.today(),'To Do'),
    Trello_items.Item('7','ITEM7',datetime.date.today(),'To Do')
    ]
#list containing only Doing items
TEST_LIST3 = [
    Trello_items.Item('1','ITEM1',datetime.date.today(),'Doing'), 
    Trello_items.Item('2','ITEM2',datetime.date.today(),'Doing'),
    Trello_items.Item('3','ITEM3',datetime.date.today(),'Doing'),
    Trello_items.Item('4','ITEM4',datetime.date.today(),'Doing'),
    Trello_items.Item('5','ITEM5',datetime.date.today(),'Doing'),
    Trello_items.Item('6','ITEM6',datetime.date.today(),'Doing'),
    Trello_items.Item('7','ITEM7',datetime.date.today(),'Doing')
    ]
#list containing only Done items
TEST_LIST4 = [
    Trello_items.Item('1','ITEM1',datetime.date.today(),'Done'), 
    Trello_items.Item('2','ITEM2',datetime.date.today(),'Done'),
    Trello_items.Item('3','ITEM3',datetime.date.today(),'Done'),
    Trello_items.Item('4','ITEM4',datetime.date.today(),'Done'),
    Trello_items.Item('5','ITEM5',datetime.date.today(),'Done'),
    Trello_items.Item('6','ITEM6',datetime.date.today(),'Done'),
    Trello_items.Item('7','ITEM7',datetime.date.today(),'Done')
    ]
#List containing missing items
TEST_LIST5 = [
    Trello_items.Item('1','ITEM1',datetime.date.today(),'Doing'), 
    Trello_items.Item('7','ITEM7',datetime.date.today(),'Done'),
    Trello_items.Item('5','ITEM5',datetime.date.today(),'Done')
    ]
#Empty list
TEST_LIST6 = [
    ]
#Done list including older items
TEST_LIST7 = [
    Trello_items.Item('1','ITEM1',datetime.date.today(),'Done'), 
    Trello_items.Item('2','ITEM2',datetime.date.today(),'Done'),
    Trello_items.Item('3','ITEM3',datetime.date.today()- datetime.timedelta(days=1),'Done'),
    Trello_items.Item('4','ITEM4',datetime.date.today(),'Done'),
    Trello_items.Item('5','ITEM5',datetime.date.today()- datetime.timedelta(days=1),'Done'),
    Trello_items.Item('6','ITEM6',datetime.date.today(),'Done'),
    Trello_items.Item('7','ITEM7',datetime.date.today(),'Done'),
    Trello_items.Item('8','ITEM8',datetime.date.today(),'Done'), 
    Trello_items.Item('9','ITEM9',datetime.date.today(),'Done'),
    Trello_items.Item('10','ITEM10',datetime.date.today()- datetime.timedelta(days=7),'Done'),
    Trello_items.Item('11','ITEM11',datetime.date.today(),'Done'),
    Trello_items.Item('12','ITEM12',datetime.date.today()- datetime.timedelta(days=100),'Done'),
    Trello_items.Item('13','ITEM13',datetime.date.today(),'Done'),
    Trello_items.Item('14','ITEM14',datetime.date.today(),'Done')
    ]
#Done list including past and future items
TEST_LIST8 = [
    Trello_items.Item('1','ITEM1',datetime.date.today(),'Done'), 
    Trello_items.Item('2','ITEM2',datetime.date.today(),'Done'),
    Trello_items.Item('3','ITEM3',datetime.date.today()+ datetime.timedelta(days=1),'Done'),
    Trello_items.Item('4','ITEM4',datetime.date.today(),'Done'),
    Trello_items.Item('5','ITEM5',datetime.date.today()+ datetime.timedelta(days=1),'Done'),
    Trello_items.Item('6','ITEM6',datetime.date.today(),'Done'),
    Trello_items.Item('7','ITEM7',datetime.date.today(),'Done'),
    Trello_items.Item('8','ITEM8',datetime.date.today(),'Done'), 
    Trello_items.Item('9','ITEM9',datetime.date.today(),'Done'),
    Trello_items.Item('10','ITEM10',datetime.date.today()- datetime.timedelta(days=7),'Done'),
    Trello_items.Item('11','ITEM11',datetime.date.today(),'Done'),
    Trello_items.Item('12','ITEM12',datetime.date.today()- datetime.timedelta(days=100),'Done'),
    Trello_items.Item('13','ITEM13',datetime.date.today(),'Done'),
    Trello_items.Item('14','ITEM14',datetime.date.today(),'Done')
    ]
TEST_LISTS = [TEST_LIST1, TEST_LIST2, TEST_LIST3, TEST_LIST4, TEST_LIST5, TEST_LIST6]
TEST_LISTS_WITH_NUMBER_OF_TODO_ITEMS = [(TEST_LIST1, 3), (TEST_LIST2, 7), (TEST_LIST3, 0), (TEST_LIST4, 0), (TEST_LIST5,0), (TEST_LIST6,0)]
TEST_LISTS_WITH_NUMBER_OF_DOING_ITEMS = [(TEST_LIST1, 2), (TEST_LIST2, 0), (TEST_LIST3, 7), (TEST_LIST4, 0), (TEST_LIST5,1), (TEST_LIST6,0)]
TEST_LISTS_WITH_NUMBER_OF_DONE_ITEMS = [(TEST_LIST1, 2), (TEST_LIST2, 0), (TEST_LIST3, 0), (TEST_LIST4, 7), (TEST_LIST5,2), (TEST_LIST6,0)]
TEST_LISTS_WITH_NUMBER_OF_RECENT_DONE_ITEMS = [(TEST_LIST1, 2), (TEST_LIST2, 0), (TEST_LIST3, 0), (TEST_LIST4, 7), (TEST_LIST5,2), (TEST_LIST6,0), (TEST_LIST7,10), (TEST_LIST8,12)]
TEST_LISTS_WITH_NUMBER_OF_OLDER_DONE_ITEMS = [(TEST_LIST1, 0), (TEST_LIST2, 0), (TEST_LIST3, 0), (TEST_LIST4, 0), (TEST_LIST5,0), (TEST_LIST6,0), (TEST_LIST7,4), (TEST_LIST8,2)]

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

@pytest.mark.parametrize("TEST_ITEMS, number_of_recent_done_items", TEST_LISTS_WITH_NUMBER_OF_RECENT_DONE_ITEMS)
def test_view_recent_done_items_contains_only_items_completed_today(TEST_ITEMS, number_of_recent_done_items):
    view = app.ViewModel(TEST_ITEMS)
    today = datetime.date.today()
    for item in view.recent_done_items:
        assert item.lastmodifieddate >= today
    assert len(view.recent_done_items) == number_of_recent_done_items

@pytest.mark.parametrize("TEST_ITEMS, number_of_older_done_items", TEST_LISTS_WITH_NUMBER_OF_OLDER_DONE_ITEMS)
def test_view_older_done_items_contains_only_items_completed_before_today(TEST_ITEMS, number_of_older_done_items):
    view = app.ViewModel(TEST_ITEMS)
    today = datetime.date.today()
    for item in view.older_done_items:
        assert item.lastmodifieddate < today
    assert len(view.older_done_items) == number_of_older_done_items
