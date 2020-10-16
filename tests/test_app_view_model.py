
def test_get_root(app, client):
    """Check a GET request to root path works"""
    response = client.get('/')
    assert response.status_code == 200
    # additional response checks go here
    raw_data = str(response.get_data())
    assert raw_data.find("<li class=\"list-group\">") > -1
