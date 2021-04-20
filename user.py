
from flask_login import UserMixin, current_user, login_required, login_user, logout_user


class User(UserMixin):
    def __init__(self, id): 
        self.id = id 
    

