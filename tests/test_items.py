import app

def test_item_status():

    TEST_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Complete', 'title': 'Allow new items to be added' },
    { 'id': 3, 'status': 'to do', 'title': 'to do item' },
    { 'id': 4, 'status': 'to do', 'title': 'to do item2' }
    ]
    view = app.ViewModel(TEST_ITEMS)
    for item in view.todoitems:
        assert item["status"] == "to do"