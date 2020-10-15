import app, Trello_items

TEST_ITEMS = [
    Trello_items.Item('1','list saved todo items','doing'), 
    Trello_items.Item('2','Allow new items to be added','Complete'),
    Trello_items.Item('3','to do item','to do'),
    Trello_items.Item('4','to do item','to do'),
    Trello_items.Item('5','to do item','Complete'),
    Trello_items.Item('6','to do item','to do'),
    Trello_items.Item('7','to do item','Doing')
    ]
def test_list_contains_only_todo_items():
    view = app.ViewModel(TEST_ITEMS)
    for item in view.todoitems:
        assert item.status == "to do"