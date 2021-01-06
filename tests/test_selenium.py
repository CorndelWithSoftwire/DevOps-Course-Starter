import os
from threading import Thread

@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable 
    board_id = create_trello_board()
    os.environ['TRELLO_BOARD_ID'] = board_id

    # construct the new application
    application = app.create_app()
    
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False)) 
    thread.daemon = True
    thread.start()
    yield app
    
    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)