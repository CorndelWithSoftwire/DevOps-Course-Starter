import io
from requests import status_codes

class MockResponsesforList(object):
    def __init__(self):
        self.status_codes ==200
        self.url = 'http://httpbin.org/get'
        self.headers = {'abcd', '1234'}

    @property
    def text(self):
        return self.json()

    def json(self):
        with io.open('tests/trelloresponses') as f:
            jsontext = f.read()
        return jsontext

class MockResponsesforCard(object):
    def __init__(self):
        self.status_codes ==200
        self.url = 'http://httpbin.org/get'
        self.headers = {'abcd', '1234'}

    @property
    def text(self):
        return self.json()

    def json(self):
        with io.open('tests/trelloresponses') as f:
            jsontext = f.read()
        return jsontext


    