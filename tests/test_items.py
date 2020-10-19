import app, Trello_items, pytest

TEST_LIST1 = [
    Trello_items.Item('1','list saved todo items','doing'), 
    Trello_items.Item('2','Allow new items to be added','Complete'),
    Trello_items.Item('3','to do item','to do'),
    Trello_items.Item('4','to do item','to do'),
    Trello_items.Item('5','to do item','Complete'),
    Trello_items.Item('6','to do item','to do'),
    Trello_items.Item('7','to do item','Doing')
    ]
TEST_LIST2 = [
    Trello_items.Item('1','list saved todo items','doing'), 
    Trello_items.Item('2','Allow new items to be added','Complete'),
    Trello_items.Item('3','to do item','to do'),
    Trello_items.Item('4','to do item','to do'),
    Trello_items.Item('5','to do item','Complete'),
    Trello_items.Item('6','to do item','to do'),
    Trello_items.Item('7','to do item','to do')
    ]
TEST_LIST3 = [
    Trello_items.Item('1','list saved todo items','doing'), 
    Trello_items.Item('2','Allow new items to be added','Complete'),
    Trello_items.Item('5','to do item','Complete'),
    ]
TEST_LISTS = [TEST_LIST1, TEST_LIST2, TEST_LIST3]

@pytest.mark.parametrize("TEST_ITEMS", TEST_LISTS)
def test_view_todoitems_contains_only_todo_items(TEST_ITEMS):
    view = app.ViewModel(TEST_ITEMS)
    for item in view.todoitems:
        assert item.status == "to do"