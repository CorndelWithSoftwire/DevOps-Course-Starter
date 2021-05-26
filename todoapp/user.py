from flask_login import UserMixin


class User(UserMixin):
    READER_ROLE = 'reader'
    WRITER_ROLE = 'writer'
    ADMIN_ROLE = 'admin'

    def __init__(self, user_id, role=READER_ROLE):
        self.id = user_id
        self.role = role

    def role(self):
        return self.role
