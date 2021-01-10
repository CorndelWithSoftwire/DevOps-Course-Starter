import pytest
from todo_app import create_app
from unittest.mock import patch
import json
from bs4 import BeautifulSoup as bs


def test_find_tests():
    assert 1 == 1


@pytest.fixture
def client():
    # Create the test app using the 'testing' config as defined in the Config.py file
    test_app = create_app('testing')
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client


def mocked_requests(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        def status_code(self):
            return self.status_code

        def raise_for_status(self):
            return None

        def ok(self):
            return "Totes"

    # get lists
    if args[0] == 'https://api.trello.com/1/boards/TEST_BOARD/lists':
        lists = '''
        [
            {"id": "5fd503e2db852a6e5a2fddab", "name": "TODO", "closed": false, "pos": 65535,
                "softLimit": null, "idBoard": "5fd503d7e780f63e718bf593", "subscribed": false},
            {"id": "5fd5044419980d052c5ba01a", "name": "DOING", "closed": false, "pos": 131071,
                "softLimit": null, "idBoard": "5fd503d7e780f63e718bf593", "subscribed": false},
            {"id": "5fd50448c2dc7974d2abed4b", "name": "DONE", "closed": false, "pos": 196607,
                "softLimit": null, "idBoard": "5fd503d7e780f63e718bf593", "subscribed": false}
        ]
        '''
        json_response = json.loads(lists)
        return MockResponse(json_response, 200)

    # get cards
    elif args[0] == "https://api.trello.com/1/boards/TEST_BOARD/cards":
        cards = '''
        [
        {"id":"5fd61710b402d20f2e8c4802","checkItemStates":null,"closed":false,"dateLastActivity":"2020-12-13T13:28:48.876Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd503e2db852a6e5a2fddab","idMembersVoted":[],"idShort":1,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Test","pos":65535,"shortLink":"ouOb3jQO","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/ouOb3jQO","start":null,"subscribed":false,"url":"https://trello.com/c/ouOb3jQO/1-test","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}},
        {"id":"5ff1c3625610c040ffe2a1b3","checkItemStates":null,"closed":false,"dateLastActivity":"2021-01-03T13:15:14.945Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd503e2db852a6e5a2fddab","idMembersVoted":[],"idShort":12,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Todo1","pos":131071,"shortLink":"8pobnhAn","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/8pobnhAn","start":null,"subscribed":false,"url":"https://trello.com/c/8pobnhAn/12-todo1","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}},
        {"id":"5ff1c368a41789899e169053","checkItemStates":null,"closed":false,"dateLastActivity":"2021-01-03T13:15:20.051Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd503e2db852a6e5a2fddab","idMembersVoted":[],"idShort":13,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Todo2","pos":196607,"shortLink":"3LnSrDts","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/3LnSrDts","start":null,"subscribed":false,"url":"https://trello.com/c/3LnSrDts/13-todo2","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}},
        {"id":"5ff1c34e70659e719b9c3af0","checkItemStates":null,"closed":false,"dateLastActivity":"2021-01-03T13:14:54.299Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd5044419980d052c5ba01a","idMembersVoted":[],"idShort":9,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Doing1","pos":65535,"shortLink":"P4g9Urdk","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/P4g9Urdk","start":null,"subscribed":false,"url":"https://trello.com/c/P4g9Urdk/9-doing1","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}},
        {"id":"5ff1c3565a26824a98e82306","checkItemStates":null,"closed":false,"dateLastActivity":"2021-01-03T13:15:02.213Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd5044419980d052c5ba01a","idMembersVoted":[],"idShort":10,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Doing2","pos":131071,"shortLink":"9OT0npwF","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/9OT0npwF","start":null,"subscribed":false,"url":"https://trello.com/c/9OT0npwF/10-doing2","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}},
        {"id":"5ff1c3597a9f1e4b9785baca","checkItemStates":null,"closed":false,"dateLastActivity":"2021-01-03T13:15:05.303Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd5044419980d052c5ba01a","idMembersVoted":[],"idShort":11,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Doing3","pos":196607,"shortLink":"cRClpz7i","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/cRClpz7i","start":null,"subscribed":false,"url":"https://trello.com/c/cRClpz7i/11-doing3","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}},
        {"id":"5feca5e4cb27193919ca8fc5","checkItemStates":null,"closed":false,"dateLastActivity":"2020-12-30T16:08:04.828Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd50448c2dc7974d2abed4b","idMembersVoted":[],"idShort":2,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Done1","pos":65535,"shortLink":"xNE8kOdD","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/xNE8kOdD","start":null,"subscribed":false,"url":"https://trello.com/c/xNE8kOdD/2-done1","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}},
        {"id":"5feca5e90e80462159a90be3","checkItemStates":null,"closed":false,"dateLastActivity":"2020-12-30T16:08:09.971Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd50448c2dc7974d2abed4b","idMembersVoted":[],"idShort":3,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Done2","pos":131071,"shortLink":"9srD0VRg","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/9srD0VRg","start":null,"subscribed":false,"url":"https://trello.com/c/9srD0VRg/3-done2","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}},
        {"id":"5feca5f1ea090949f317af96","checkItemStates":null,"closed":false,"dateLastActivity":"2020-12-30T16:08:17.632Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd50448c2dc7974d2abed4b","idMembersVoted":[],"idShort":4,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Done3","pos":196607,"shortLink":"YPboQyw0","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/YPboQyw0","start":null,"subscribed":false,"url":"https://trello.com/c/YPboQyw0/4-done3","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}},
        {"id":"5feca5fe90b3533211957225","checkItemStates":null,"closed":false,"dateLastActivity":"2020-12-30T16:08:30.276Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd50448c2dc7974d2abed4b","idMembersVoted":[],"idShort":5,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Done4","pos":262143,"shortLink":"HsLEp764","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/HsLEp764","start":null,"subscribed":false,"url":"https://trello.com/c/HsLEp764/5-done4","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}},
        {"id":"5feca603641fc384843aed66","checkItemStates":null,"closed":false,"dateLastActivity":"2020-12-30T16:08:35.597Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd50448c2dc7974d2abed4b","idMembersVoted":[],"idShort":6,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Done5","pos":327679,"shortLink":"h97mNEc8","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/h97mNEc8","start":null,"subscribed":false,"url":"https://trello.com/c/h97mNEc8/6-done5","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}},
        {"id":"5feca6078f88ec4fba621296","checkItemStates":null,"closed":false,"dateLastActivity":"2020-12-29T16:08:39.489Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd50448c2dc7974d2abed4b","idMembersVoted":[],"idShort":7,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Done6","pos":393215,"shortLink":"Ferb54WM","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/Ferb54WM","start":null,"subscribed":false,"url":"https://trello.com/c/Ferb54WM/7-done6","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}},
        {"id":"5feca60a6174285cd6f17b5a","checkItemStates":null,"closed":false,"dateLastActivity":"2020-12-28T16:08:42.698Z","desc":"","descData":null,"dueReminder":null,"idBoard":"5fd503d7e780f63e718bf593","idList":"5fd50448c2dc7974d2abed4b","idMembersVoted":[],"idShort":8,"idAttachmentCover":null,"idLabels":[],"manualCoverAttachment":false,"name":"Done7","pos":458751,"shortLink":"tVynx2Kv","isTemplate":false,"cardRole":null,"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":false,"votes":0,"viewingMemberVoted":false,"subscribed":false,"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"attachments":0,"description":false,"due":null,"dueComplete":false,"start":null},"dueComplete":false,"due":null,"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/tVynx2Kv","start":null,"subscribed":false,"url":"https://trello.com/c/tVynx2Kv/8-done7","cover":{"idAttachment":null,"color":null,"idUploadedBackground":null,"size":"normal","brightness":"light"}}
        ]
        '''
        json_response = json.loads(cards)
        return MockResponse(json_response, 200)

    # get card
    elif args[0] == 'https://api.trello.com/1/cards/5feca60a6174285cd6f17b5a':
        card = '{"id": "5feca60a6174285cd6f17b5a", "checkItemStates": [], "closed": false, "dateLastActivity": "2020-10-11T19:20:28.624Z", "desc": "This is a test task for a new item", "descData": null, "dueReminder": null, "idBoard": "5fd503d7e780f63e718bf593", "idList": "5fd50448c2dc7974d2abed4b", "idMembersVoted": [], "idShort": 63, "idAttachmentCover": null, "idLabels": [], "manualCoverAttachment": false, "name": "New Test Task", "pos": 32768, "shortLink": "iUihslfg", "isTemplate": false, "dueComplete": false, "due": "2020-10-30T00:00:00.000Z", "labels": [], "shortUrl": "https://trello.com/c/iUihslfg", "start": null,"url": "https://trello.com/c/iUihslfg/63-new-test-task", "cover": {"idAttachment": null, "color": null, "idUploadedBackground": null, "size": "normal", "brightness": "light"}, "idMembers": [], "email": null, "badges": {"attachmentsByType": {"trello": {"board": 0, "card": 0}}, "location": false, "votes": 0, "viewingMemberVoted": false, "subscribed": false, "fogbugz": "", "checkItems": 0, "checkItemsChecked": 0, "checkItemsEarliestDue": null, "comments": 0, "attachments": 0, "description": true, "due": "2020-10-30T00:00:00.000Z", "dueComplete": false, "start": null}, "subscribed": false, "idChecklists": []}'
        json_response = json.loads(card)
        return MockResponse(json_response, 200)

    return MockResponse(None, 404)


@patch('requests.get', side_effect=mocked_requests)
def test_index_page(mocked_requests, client):
    response = client.get('/')
    assert response.status_code == 200


@patch('requests.get', side_effect=mocked_requests)
def test_index_page(mocked_requests, client):
    response = client.get('/')
    soup = bs(response.data, "html.parser")
    titles = [i.contents[0] for i in soup.find_all(class_="card-title")]
    assert titles == ['Test', 'Todo1', 'Todo2', 'Doing1', 'Doing2', 'Doing3',
                      'Done1', 'Done2', 'Done3', 'Done4', 'Done5', 'Done6', 'Done7']


@ patch('requests.get', side_effect=mocked_requests)
def test_card_page(mocked_requests, client):
    response = client.get('card/5feca60a6174285cd6f17b5a')
    assert response.status_code == 200
