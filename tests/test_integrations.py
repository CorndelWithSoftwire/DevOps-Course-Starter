import app, pytest, Trello_items
from dotenv import find_dotenv, load_dotenv

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

class mock_get_lists_response:
    @staticmethod
    def json():
        null=None; false=False
        listsjson = ([
        {
            "id":"fake_trello_todo_listid",
            "name":"To Do",
            "closed":false,
            "pos":65535,
            "softLimit":null,
            "idBoard":"fake_trello_boardid",
            "subscribed":false
        },
        {
            "id":"fake_trello_doing_listid",
            "name":"Doing","closed":false,
            "pos":131071,
            "softLimit":null,
            "idBoard":"fake_trello_boardid",
            "subscribed":false
        },
        {
            "id":"fake_trello_done_listid",
            "name":"Done",
            "closed":false,
            "pos":196607,
            "softLimit":null,
            "idBoard":"fake_trello_boardid",
            "subscribed":false
        }
        ]
        )
        return listsjson

class mock_get_response:
    @staticmethod
    def json():
        null=None; false=False
        cardsjson = ([
        {
            "id": "5f6077112123754226d45e70",
            "checkItemStates": null,
            "closed": false,
            "dateLastActivity": "2020-10-20T08:37:11.563Z",
            "desc": "",
            "descData": null,
            "dueReminder": null,
            "idBoard": "fake_trello_boardid",
            "idList": "fake_trello_todo_listid",
            "idMembersVoted": [],
            "idShort": 1,
            "idAttachmentCover": null,
            "idLabels": [],
            "manualCoverAttachment": false,
            "name": "TestItem1",
            "pos": 4096,
            "shortLink": "RkbH2NXg",
            "isTemplate": false,
            "badges": {
                "attachmentsByType": {
                    "trello": {
                        "board": 0,
                        "card": 0
                    }
                },
                "location": false,
                "votes": 0,
                "viewingMemberVoted": false,
                "subscribed": false,
                "fogbugz": "",
                "checkItems": 0,
                "checkItemsChecked": 0,
                "checkItemsEarliestDue": null,
                "comments": 0,
                "attachments": 0,
                "description": false,
                "due": null,
                "dueComplete": false,
                "start": null
            },
            "dueComplete": false,
            "due": null,
            "idChecklists": [],
            "idMembers": [],
            "labels": [],
            "shortUrl": "https://trello.com/c/RkbH2NXg",
            "start": null,
            "subscribed": false,
            "url": "https://trello.com/c/RkbH2NXg/1-TestItem1",
            "cover": {
                "idAttachment": null,
                "color": null,
                "idUploadedBackground": null,
                "size": "normal",
                "brightness": "light"
            }
        },
        {
            "id": "5f8f1a26093ea07eff6678c6",
            "checkItemStates": null,
            "closed": false,
            "dateLastActivity": "2020-10-21T07:14:24.214Z",
            "desc": "",
            "descData": null,
            "dueReminder": null,
            "idBoard": "fake_trello_boardid",
            "idList": "fake_trello_todo_listid",
            "idMembersVoted": [],
            "idShort": 33,
            "idAttachmentCover": null,
            "idLabels": [],
            "manualCoverAttachment": false,
            "name": "TestItem2",
            "pos": 53248,
            "shortLink": "c0SpYMfi",
            "isTemplate": false,
            "badges": {
                "attachmentsByType": {
                    "trello": {
                        "board": 0,
                        "card": 0
                    }
                },
                "location": false,
                "votes": 0,
                "viewingMemberVoted": false,
                "subscribed": false,
                "fogbugz": "",
                "checkItems": 0,
                "checkItemsChecked": 0,
                "checkItemsEarliestDue": null,
                "comments": 0,
                "attachments": 0,
                "description": false,
                "due": null,
                "dueComplete": false,
                "start": null
            },
            "dueComplete": false,
            "due": null,
            "idChecklists": [],
            "idMembers": [],
            "labels": [],
            "shortUrl": "https://trello.com/c/c0SpYMfi",
            "start": null,
            "subscribed": false,
            "url": "https://trello.com/c/c0SpYMfi/33-TestItem2",
            "cover": {
                "idAttachment": null,
                "color": null,
                "idUploadedBackground": null,
                "size": "normal",
                "brightness": "light"
            }
        },
        {
            "id": "5f8f0b9427cf9183e7ec00bb",
            "checkItemStates": null,
            "closed": false,
            "dateLastActivity": "2020-10-21T07:14:27.913Z",
            "desc": "",
            "descData": null,
            "dueReminder": null,
            "idBoard": "fake_trello_boardid",
            "idList": "fake_trello_done_listid",
            "idMembersVoted": [],
            "idShort": 30,
            "idAttachmentCover": null,
            "idLabels": [],
            "manualCoverAttachment": false,
            "name": "TestItem3",
            "pos": 122879.25,
            "shortLink": "k6O8zK5g",
            "isTemplate": false,
            "badges": {
                "attachmentsByType": {
                    "trello": {
                        "board": 0,
                        "card": 0
                    }
                },
                "location": false,
                "votes": 0,
                "viewingMemberVoted": false,
                "subscribed": false,
                "fogbugz": "",
                "checkItems": 0,
                "checkItemsChecked": 0,
                "checkItemsEarliestDue": null,
                "comments": 0,
                "attachments": 0,
                "description": false,
                "due": null,
                "dueComplete": false,
                "start": null
            },
            "dueComplete": false,
            "due": null,
            "idChecklists": [],
            "idMembers": [],
            "labels": [],
            "shortUrl": "https://trello.com/c/k6O8zK5g",
            "start": null,
            "subscribed": false,
            "url": "https://trello.com/c/k6O8zK5g/30-TestItem3",
            "cover": {
                "idAttachment": null,
                "color": null,
                "idUploadedBackground": null,
                "size": "normal",
                "brightness": "light"
            }
        },
        {
            "id": "5f8f1a1d627fef8ed02c2f63",
            "checkItemStates": null,
            "closed": false,
            "dateLastActivity": "2020-10-21T07:14:22.834Z",
            "desc": "",
            "descData": null,
            "dueReminder": null,
            "idBoard": "fake_trello_boardid",
            "idList": "fake_trello_doing_listid",
            "idMembersVoted": [],
            "idShort": 32,
            "idAttachmentCover": null,
            "idLabels": [],
            "manualCoverAttachment": false,
            "name": "TestItem4",
            "pos": 36864,
            "shortLink": "pDXcqiUi",
            "isTemplate": false,
            "badges": {
                "attachmentsByType": {
                    "trello": {
                        "board": 0,
                        "card": 0
                    }
                },
                "location": false,
                "votes": 0,
                "viewingMemberVoted": false,
                "subscribed": false,
                "fogbugz": "",
                "checkItems": 0,
                "checkItemsChecked": 0,
                "checkItemsEarliestDue": null,
                "comments": 0,
                "attachments": 0,
                "description": false,
                "due": null,
                "dueComplete": false,
                "start": null
            },
            "dueComplete": false,
            "due": null,
            "idChecklists": [],
            "idMembers": [],
            "labels": [],
            "shortUrl": "https://trello.com/c/pDXcqiUi",
            "start": null,
            "subscribed": false,
            "url": "https://trello.com/c/pDXcqiUi/32-TestItem4",
            "cover": {
                "idAttachment": null,
                "color": null,
                "idUploadedBackground": null,
                "size": "normal",
                "brightness": "light"
            }
        }
        ]
        )   
        return cardsjson 



def test_index_page(client, monkeypatch):
    def mock_get_requests(*args, **kwargs):
        if args[0] == 'https://api.trello.com/1/boards/fake_trello_boardid/lists':
            return mock_get_lists_response
        else:
            return mock_get_response
    monkeypatch.setattr(Trello_items.requests, "get", mock_get_requests)
    response = client.get('/')
    assert "TestItem1" in str(response.data)
    assert "TestItem2" in str(response.data)
    assert "TestItem3" in str(response.data)
    assert "TestItem4" in str(response.data)
