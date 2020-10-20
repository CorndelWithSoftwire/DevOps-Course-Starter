
def test_get_root(client):
    """Check a GET request to root path works"""
    response = client.get('/')

