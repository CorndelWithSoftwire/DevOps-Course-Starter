from app.to_do_item import ToDoItem

class TestToDoItem:
    def test_to_do_item_str(self):
        item = ToDoItem('123', 'To Do', 'Title', '2021-01-06T21:14:06.518Z')

        assert str(item) == 'Title-To Do-2021-01-06T21:14:06.518Z'