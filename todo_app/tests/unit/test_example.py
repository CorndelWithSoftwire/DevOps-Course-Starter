import requests
import unittest, pytest
from unittest import mock

# This is the class we want to test
class MyGreatClass:
    def fetch_json(self, url):
        response = requests.get(url)
        return response.json()

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'todo_app\tests\response_Cards.json':
        return MockResponse({"id":"6054b0101e6a3d49645dbdc9","name":"To Do","pos":16384,"idBoard":"6054b0101e6a3d49645dbdc8"}, 200)
    return MockResponse(None, 404)

# Our test case class
class MyGreatClassTestCase(unittest.TestCase):

    # We patch 'requests.get' with our own method. The mock object is passed in to our test case method.
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch(self, mock_get):
        # Assert requests.get calls
        mgc = MyGreatClass()
        json_data = mgc.fetch_json('todo_app\tests\response_Cards.json')
        self.assertEqual(json_data, {"id":"6054b0101e6a3d49645dbdc9","name":"To Do","pos":16384,"idBoard":"6054b0101e6a3d49645dbdc8"})
               # We can even assert that our mocked method was called with the right parameters
        self.assertIn(mock.call('todo_app\tests\response_Cards.json'), mock_get.call_args_list)
       
        self.assertEqual(len(mock_get.call_args_list), 1)

