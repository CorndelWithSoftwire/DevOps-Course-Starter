import pytest
import view_model as view_model
import datetime
from task import Task
    
@pytest.fixture
def test_tasks():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    task_list = [
        Task(1, 'To Do', 'Task1', str(today)),
        Task(2, 'To Do', 'Task2', str(today)),
        Task(3, 'Doing', 'Task3', str(today)),
        Task(4, 'Doing', 'Task4', str(today)),
        Task(5, 'Doing', 'Task5', str(today)),
        Task(6, 'Done', 'Task6', str(today)),
        Task(7, 'Done', 'Task7', str(today)),
        Task(8, 'Done', 'Task8', str(today)),
        Task(9, 'Done', 'Task8', str(today)),
        Task(10, 'Done', 'Task10', str(yesterday)),
        Task(11, 'Done', 'Task11', str(yesterday)),
        Task(12, 'Done', 'Task12', str(yesterday))
    ]

    test_list = view_model.ViewModel(task_list)

    return test_list

@pytest.fixture
def test_tasks_2():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days= 1)
    task_list = [ 
        Task(1, 'To Do', 'Task1', str(today)),
        Task(2, 'To Do', 'Task2', str(today)),
        Task(3, 'Doing', 'Task3', str(today)),
        Task(4, 'Doing', 'Task4', str(today)),
        Task(5, 'Done', 'Task5', str(today)),
        Task(6, 'Done', 'Task6', str(yesterday)),
        Task(7, 'Done', 'Task7', str(yesterday)),
        Task(8, 'Done', 'Task8', str(yesterday))
    ]
    
    test_list = view_model.ViewModel(task_list)

    return test_list

@pytest.fixture
def test_tasks_3():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days= 1)
    task_list = [   
        Task(1, 'Doing', 'Task1', str(today)),
        Task(2, 'Doing', 'Task2', str(today)),
        Task(3, 'Done', 'Task3', str(today)),
        Task(4, 'Done', 'Task4', str(today)),
        Task(5, 'Done', 'Task5', str(today)),
        Task(6, 'Done', 'Task6', str(yesterday)),
        Task(7, 'Done', 'Task7', str(yesterday))
    ]

    test_list = view_model.ViewModel(task_list)

    return test_list

def test_to_do_items_count(test_tasks):
    todo = test_tasks.todo_tasks
    assert len(todo) == 2

def test_doing_items_count(test_tasks):
    doing = test_tasks.doing_tasks
    assert len(doing) == 3

def test_done_items_count(test_tasks):
    done = test_tasks.done_tasks
    assert len(done) == 7

def test_recent_done_items_count(test_tasks):
    today_tasks = test_tasks.recent_done_tasks
    assert len(today_items) == 4

def test_older_done_items_count(test_tasks):
    older_tasks = test_tasks.older_done_tasks
    assert len(older_tasks) == 3

def test_show_all_tasks_more_than_5(test_tasks):
    show_all = test_tasks.show_all_done
    assert len(show_all) == 4

def test_show_all_items_less_than_5(test_tasks_2):
    show_all = test_tasks_2.show_all_done
    assert len(show_all) == 4

def test_show_all_items_equal_to_5(test_tasks_3):
    show_all = test_tasks_3.show_all_done
    assert len(show_all) == 5