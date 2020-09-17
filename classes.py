class todo_status:

    def __init__(self, trello_id, status):
        self.trello_id = trello_id
        self.status = status
        
    def __str__(self):
        return "({0}, {1})".format(self.trello_id, self.status)




class todo_item:

    def __init__(self, trello_id, title, description, due_date, status):
        self.trello_id = trello_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
