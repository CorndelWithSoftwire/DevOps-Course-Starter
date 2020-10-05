import os

class Card:
    def __init__(self, id, name, list_id):
        self.id = id
        self.name = name

        todo_list_id = os.getenv('TRELLO_TODO_ID')
        doing_list_id = os.getenv('TRELLO_DOING_ID')
        done_list_id = os.getenv('TRELLO_DONE_ID')
        
        if list_id == todo_list_id:
            self.status = "Things Todo"
        elif list_id == doing_list_id:
            self.status = "Doing"
        else:
            self.status = "Done"
