from tests.mock_trello_data import mock_trello_handler

def test_get_root(client, monkeypatch):
    mock_trello_handler(monkeypatch)
    """Check a GET request to root path works"""
    response = client.get('/')
    assert response.status_code == 200
    assert str(response.data).find('/update_todo/5f6a132be45bd103bdaa16a9') > 0
    assert str(response.data).find('test sunday') > 0


