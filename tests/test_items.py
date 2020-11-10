import Trello_items, pytest, datetime
import viewmodel as vm


test_list_mixture_of_items = [
    Trello_items.Item('1','ITEM1',datetime.date.today(),'Doing'), 
    Trello_items.Item('2','ITEM2',datetime.date.today(),'Done'),
    Trello_items.Item('3','ITEM3',datetime.date.today(),'To Do'),
    Trello_items.Item('4','ITEM4',datetime.date.today(),'To Do'),
    Trello_items.Item('5','ITEM5',datetime.date.today(),'Done'),
    Trello_items.Item('6','ITEM6',datetime.date.today(),'To Do'),
    Trello_items.Item('7','ITEM7',datetime.date.today(),'Doing')
    ]

test_list_only_todo_items = [
    Trello_items.Item('1','ITEM1',datetime.date.today(),'To Do'), 
    Trello_items.Item('2','ITEM2',datetime.date.today(),'To Do'),
    Trello_items.Item('3','ITEM3',datetime.date.today(),'To Do'),
    Trello_items.Item('4','ITEM4',datetime.date.today(),'To Do'),
    Trello_items.Item('5','ITEM5',datetime.date.today(),'To Do'),
    Trello_items.Item('6','ITEM6',datetime.date.today(),'To Do'),
    Trello_items.Item('7','ITEM7',datetime.date.today(),'To Do')
    ]

test_list_only_doing_items = [
    Trello_items.Item('1','ITEM1',datetime.date.today(),'Doing'), 
    Trello_items.Item('2','ITEM2',datetime.date.today(),'Doing'),
    Trello_items.Item('3','ITEM3',datetime.date.today(),'Doing'),
    Trello_items.Item('4','ITEM4',datetime.date.today(),'Doing'),
    Trello_items.Item('5','ITEM5',datetime.date.today(),'Doing'),
    Trello_items.Item('6','ITEM6',datetime.date.today(),'Doing'),
    Trello_items.Item('7','ITEM7',datetime.date.today(),'Doing')
    ]

test_list_only_done_items = [
    Trello_items.Item('1','ITEM1',datetime.date.today(),'Done'), 
    Trello_items.Item('2','ITEM2',datetime.date.today(),'Done'),
    Trello_items.Item('3','ITEM3',datetime.date.today(),'Done'),
    Trello_items.Item('4','ITEM4',datetime.date.today(),'Done'),
    Trello_items.Item('5','ITEM5',datetime.date.today(),'Done'),
    Trello_items.Item('6','ITEM6',datetime.date.today(),'Done'),
    Trello_items.Item('7','ITEM7',datetime.date.today(),'Done')
    ]

test_list_missing_ids_items = [
    Trello_items.Item('1','ITEM1',datetime.date.today(),'Doing'), 
    Trello_items.Item('7','ITEM7',datetime.date.today(),'Done'),
    Trello_items.Item('5','ITEM5',datetime.date.today(),'Done')
    ]

test_list_empty = [
    ]

test_list_done_items_with_older_items = [
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

test_list_done_items_with_past_and_future_items = [
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
test_lists = [test_list_mixture_of_items, test_list_only_todo_items, test_list_only_doing_items, test_list_only_done_items, test_list_missing_ids_items, test_list_empty]
test_lists_with_number_of_todo_items = [(test_list_mixture_of_items, 3), (test_list_only_todo_items, 7), (test_list_only_doing_items, 0), (test_list_only_done_items, 0), (test_list_missing_ids_items,0), (test_list_empty,0)]
test_lists_with_number_of_doing_items = [(test_list_mixture_of_items, 2), (test_list_only_todo_items, 0), (test_list_only_doing_items, 7), (test_list_only_done_items, 0), (test_list_missing_ids_items,1), (test_list_empty,0)]
test_lists_with_number_of_done_items = [(test_list_mixture_of_items, 2), (test_list_only_todo_items, 0), (test_list_only_doing_items, 0), (test_list_only_done_items, 7), (test_list_missing_ids_items,2), (test_list_empty,0)]
test_lists_with_number_of_recent_done_items = [(test_list_mixture_of_items, 2), (test_list_only_todo_items, 0), (test_list_only_doing_items, 0), (test_list_only_done_items, 7), (test_list_missing_ids_items,2), (test_list_empty,0), (test_list_done_items_with_older_items,10), (test_list_done_items_with_past_and_future_items,12)]
test_lists_with_number_of_older_done_items = [(test_list_mixture_of_items, 0), (test_list_only_todo_items, 0), (test_list_only_doing_items, 0), (test_list_only_done_items, 0), (test_list_missing_ids_items,0), (test_list_empty,0), (test_list_done_items_with_older_items,4), (test_list_done_items_with_past_and_future_items,2)]

@pytest.mark.parametrize("TEST_ITEMS", test_lists)
def test_view_todoitems_contains_only_todo_items(TEST_ITEMS):
    view = vm.ViewModel(TEST_ITEMS)
    for item in view.todoitems:
        assert item.status == "To Do"

@pytest.mark.parametrize("TEST_ITEMS, number_of_todo_items", test_lists_with_number_of_todo_items)
def test_view_todoitems_contains_correct_number_of_items(TEST_ITEMS, number_of_todo_items):
    view = vm.ViewModel(TEST_ITEMS)   
    assert len(view.todoitems) == number_of_todo_items

@pytest.mark.parametrize("TEST_ITEMS", test_lists)
def test_view_doingitems_contains_only_doing_items(TEST_ITEMS):
    view = vm.ViewModel(TEST_ITEMS)
    for item in view.doingitems:
        assert item.status == "Doing"

@pytest.mark.parametrize("TEST_ITEMS, number_of_doing_items", test_lists_with_number_of_doing_items)
def test_view_doingitems_contains_correct_number_of_items(TEST_ITEMS, number_of_doing_items):
    view = vm.ViewModel(TEST_ITEMS)   
    assert len(view.doingitems) == number_of_doing_items

@pytest.mark.parametrize("TEST_ITEMS", test_lists)
def test_view_show_all_done_items_contains_only_done_items(TEST_ITEMS):
    view = vm.ViewModel(TEST_ITEMS)
    for item in view.show_all_done_items:
        assert item.status == "Done"

@pytest.mark.parametrize("TEST_ITEMS, number_of_done_items", test_lists_with_number_of_done_items)
def test_view_show_all_done_items_contains_correct_number_of_items(TEST_ITEMS, number_of_done_items):
    view = vm.ViewModel(TEST_ITEMS)   
    assert len(view.show_all_done_items) == number_of_done_items

@pytest.mark.parametrize("TEST_ITEMS, number_of_recent_done_items", test_lists_with_number_of_recent_done_items)
def test_view_recent_done_items_contains_only_items_completed_today(TEST_ITEMS, number_of_recent_done_items):
    view = vm.ViewModel(TEST_ITEMS)
    today = datetime.date.today()
    for item in view.recent_done_items:
        assert item.lastmodifieddate >= today
    assert len(view.recent_done_items) == number_of_recent_done_items

@pytest.mark.parametrize("TEST_ITEMS, number_of_older_done_items", test_lists_with_number_of_older_done_items)
def test_view_older_done_items_contains_only_items_completed_before_today(TEST_ITEMS, number_of_older_done_items):
    view = vm.ViewModel(TEST_ITEMS)
    today = datetime.date.today()
    for item in view.older_done_items:
        assert item.lastmodifieddate < today
    assert len(view.older_done_items) == number_of_older_done_items
