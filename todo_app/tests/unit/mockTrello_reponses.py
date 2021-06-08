import io
from requests import status_codes

class MockResponsesforList(object):
    def __init__(self):
        self.status_code == 200
        self.url = 'http://httpbin.org/get'
        self.headers = {'abcd', '1234'}

    @property
    def text(self):
        return self.json()

    def json(self):
        with io.open('todo_app/tests/response_list.json') as f:
            jsontext = f.read()
        return jsontext

class MockResponsesforCard(object):
    def __init__(self):
        self.status_code == 200
        self.url = 'http://httpbin.org/get'
        self.headers = {'abcd', '1234'}

    @property
    def text(self):
        return self.json()

    def json(self):
        with io.open('todo_app/tests/response_list.json') as f:
            jsontext = f.read()
        return jsontext


    