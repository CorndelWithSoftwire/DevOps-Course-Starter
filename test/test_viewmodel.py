from typing import List
from app.viewmodel import ViewModel
from app.to_do_item import ToDoItem
from datetime import datetime, timedelta

class TestViewModel:
    def test_items(self):
        first_item = ToDoItem("1234", "To Do", "First Test Item", '2021-01-06T21:14:06.518Z')
        second_item = ToDoItem("4321", "Doing", "In progress Item", '2021-01-06T21:14:06.518Z')

        item_list = [first_item, second_item]

        view_model_under_test = ViewModel(item_list)

        assert view_model_under_test.items == item_list

    def test_to_do(self):
        first_item = ToDoItem("1234", "To Do", "First Test Item", '2021-01-06T21:14:06.518Z')
        second_item = ToDoItem("4321", "Doing", "In progress Item", '2021-01-06T21:14:06.518Z')
        third_item = ToDoItem("1111", "Done", "I hope this test passes", '2021-01-06T21:14:06.518Z')

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list)

        assert view_model_under_test.to_do == [first_item]

    def test_doing(self):
        first_item = ToDoItem("1234", "To Do", "First Test Item", '2021-01-06T21:14:06.518Z')
        second_item = ToDoItem("4321", "Doing", "In progress Item", '2021-01-06T21:14:06.518Z')
        third_item = ToDoItem("1111", "Done", "I hope this test passes", '2021-01-06T21:14:06.518Z')

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list)

        assert view_model_under_test.doing == [second_item]

    def test_done(self):
        first_item = ToDoItem("1234", "To Do", "First Test Item", '2021-01-06T21:14:06.518Z')
        second_item = ToDoItem("4321", "Doing", "In progress Item", '2021-01-06T21:14:06.518Z')
        third_item = ToDoItem("1111", "Done", "I hope this test passes", '2021-01-06T21:14:06.518Z')

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list)

        assert view_model_under_test.done == [third_item]

    def test_show_all_done_items_more_than_five(self):
        today = datetime.now()
        yesterday = datetime.now() + timedelta(days=-1)

        one = ToDoItem("1", "Done", "One", today)
        two = ToDoItem("2", "Done", "One", today)
        three = ToDoItem("3", "Done", "One", yesterday)
        four = ToDoItem("4", "Done", "One", yesterday)
        five = ToDoItem("5", "Done", "One", yesterday)
        six = ToDoItem("6", "Done", "One", yesterday)

        item_list = [one, two, three, four, five, six]

        view_model_under_test = ViewModel(item_list)

        assert view_model_under_test.show_all_done_items == [one, two]

    def test_show_all_done_items_less_than_five(self):
        today = datetime.now()
        yesterday = datetime.now() + timedelta(days=-1)

        one = ToDoItem("1", "Done", "One", today)
        two = ToDoItem("2", "Done", "One", today)
        three = ToDoItem("3", "Done", "One", yesterday)
        four = ToDoItem("4", "Done", "One", yesterday)

        item_list = [one, two, three, four]

        view_model_under_test = ViewModel(item_list)

        assert view_model_under_test.show_all_done_items == [one, two, three, four]

    def test_recent_done_items(self):
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        yesterday = today + timedelta(days=-1)

        first_item = ToDoItem("1234", "Done", "First Test Item", yesterday)
        second_item = ToDoItem("4321", "Done", "In progress Item", today)
        third_item = ToDoItem("1111", "Done", "I hope this test passes", tomorrow)

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list)
        assert view_model_under_test.recent_done_items == [second_item]

    def test_older_done_items(self):
        today = datetime.now()
        yesterday = today + timedelta(days=-1)

        first_item = ToDoItem("1234", "Done", "First Test Item", yesterday)
        second_item = ToDoItem("4321", "Done", "In progress Item", today)
        third_item = ToDoItem("1111", "Done", "I hope this test passes", yesterday)

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list)
        assert view_model_under_test.older_done_items == [first_item, third_item]