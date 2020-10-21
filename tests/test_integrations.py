import app, Trello_items, pytest, datetime
from dotenv import find_dotenv, load_dotenv

TRELLO_TODO_LISTID = os.environ.get('TRELLO_TODO_LISTID')
TRELLO_DOING_LISTID = os.environ.get('TRELLO_DOING_LISTID')
TRELLO_DONE_LISTID = os.environ.get('TRELLO_DONE_LISTID')

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
