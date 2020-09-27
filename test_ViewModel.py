import pytest


from model import Item, ViewModel

def test_items():
    assert len(get_test_items()) == len(get_test_view_model().items)
    

def test_to_do_items():
    assert len(get_test_view_model().todoItems) == 1

def test_doing_items():
    assert len(get_test_view_model().doingItems) == 1

def test_done_items():
    assert len(get_test_view_model().doneItems) == 1

def get_test_items():
    item1 = Item('5f5a4c01846bb381f6f3fa8b', 'To Do', 'To Do 111')
    item2= Item('5f6f50a13a48c95efb5679f1', 'Doing', 'To Do 222')
    item3 = Item('5f6f50cc2316514d6241e6ba', 'Done', 'To Do 333')
    testListItems = list()
    testListItems.append(item1)
    testListItems.append(item2)
    testListItems.append(item3)
    return testListItems

def get_test_view_model():
    testViewModel = ViewModel(get_test_items())
    return testViewModel
