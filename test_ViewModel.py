import pytest
from datetime import datetime, timedelta


from model import Item, ViewModel

def test_items():
    assert len(get_test_items()) == len(get_test_view_model().items)
    

def test_to_do_items():
    assert len(get_test_view_model().todoItems) == 1

def test_to_do_items_values():
    for item in get_test_view_model().todoItems:
        id, status, title = item.id, item.status, item.title
        assert id == '5f5a4c01846bb381f6f3fa8b' and status == 'To Do' and title == 'To Do 111'

def test_doing_items():
    assert len(get_test_view_model().doingItems) == 1

def test_doing_items_values():
    for item in get_test_view_model().doingItems:
        id, status, title = item.id, item.status, item.title
        assert id == '5f6f50a13a48c95efb5679f1' and status == 'Doing' and title == 'To Do 222'
        
def test_done_items():
    assert len(get_test_view_model().doneItems) == 2

def test_done_items_values():
    for item in get_test_view_model().doneItems:
        id, status, title = item.id, item.status, item.title
        assert id == '5f6f50cc2316514d6241e6ba' and status == 'Done'
        #assert id == '5f6f50cc2316514d6241e6ba' and status == 'Done' and title == 'To Do 333'

def test_recent_done_items():
    assert len(get_test_view_model().recent_done_items) == 1

def test_recent_done_items_values():
    for item in get_test_view_model().recent_done_items:
        id, status, title = item.id, item.status, item.title
        assert id == '5f6f50cc2316514d6241e6ba' and status == 'Done' and title == 'To Do 333'

def test_older_done_items():
    assert len(get_test_view_model().older_done_items) == 1

def test_older_done_items_values():
    for item in get_test_view_model().older_done_items:
        id, status, title = item.id, item.status, item.title
        assert id == '5f6f50cc2316514d6241e6ba' and status == 'Done' and title == 'To Do 444'


def get_test_items():
    item1 = Item('5f5a4c01846bb381f6f3fa8b', 'To Do', 'To Do 111')
    item2= Item('5f6f50a13a48c95efb5679f1', 'Doing', 'To Do 222')
    item3 = Item('5f6f50cc2316514d6241e6ba', 'Done', 'To Do 333')
    item4 = Item('5f6f50cc2316514d6241e6ba', 'Done', 'To Do 444', (datetime.now() - timedelta(1)).strftime('%Y-%m-%d'))
    
    testListItems = list()
    testListItems.append(item1)
    testListItems.append(item2)
    testListItems.append(item3)
    testListItems.append(item4)
    return testListItems

def get_test_view_model():
    testViewModel = ViewModel(get_test_items())
    return testViewModel
