from flask_config import Config


class Item:

    def __init__(self, response):
        self.title = response['name']
        self.status = 'Completed' if Config.DONE_LIST_ID == response['idList'] else 'Not Started'
        self.id = response['id']
        self.desc = response['desc']