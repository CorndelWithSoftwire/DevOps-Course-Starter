import dateutil.parser

class Task:
    def __init__(self, id, status, title, last_modified):
        self.id = id
        self.title = title
        self.status = status
        self.last_modified = last_modified