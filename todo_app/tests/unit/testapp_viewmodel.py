from todo_app.tests.unit.mockTrello_data import monkey_trello

def test_getroot(client, monkeypatch):
    monkey_trello(monkeypatch)
    response = client.get('/')
    assert response.status_code ==200
    assert str(response.data).find('/todolist/6054b0101e6a3d49645dbdc8') > 0