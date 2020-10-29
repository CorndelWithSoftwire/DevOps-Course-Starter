import datetime

class ViewModel:     
    def __init__(self, tasks):   
        self._tasks = tasks   

    @property
    def tasks(self):
        return self._tasks 

    @property
    def tasks_todo(self):
        todo = [task for task in self._tasks if task.status == 'To Do']
        return todo

    @property
    def tasks_doing(self):
        doing = [task for task in self._tasks if task.status == 'Doing']
        return doing

    @property
    def tasks_done(self):
        done = [task for task in self._tasks if task.status == 'Done']
        return done
    
    @property
    def tasks_recently_done(self):
        done = self.tasks_done
        today = datetime.date.today()
        today_list = [task for task in done if task.last_modified.date() == today]
        return today_list

    @property
    def older_done_tasks(self):        
        done = self.tasks_done   
        today = datetime.date.today()     
        today_list = [task for task in done if task.last_modified.date() < today]
        return today_list

    @property
    def show_all_done_tasks(self):
        done = self.tasks_done
        today = datetime.date.today()
        if len(done) <= 5:
            return done
        else:            
            recent_list = [task for task in done if task.last_modified.date() == today]
            return recent_list

    def last_modified_today_tasks(self, tasks):
        today = datetime.date.today()
        today_list = [task for task in tasks if task.last_modified.date() == today]
        return today_list

    def last_modified_less_than_today_tasks(self, tasks):
        today = datetime.date.today()
        today_list = [task for task in tasks if task.last_modified.date() < today]
        return today_list
