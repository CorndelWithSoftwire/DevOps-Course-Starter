import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration variables."""
    TESTING = False
    TRELLO_KEY = os.environ.get('TRELLO_KEY')
    TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
    TRELLO_BOARD = os.environ.get('TRELLO_BOARD')


class TestingConfig(Config):
    """Test configuration variables."""
    TESTING = True
    #TRELLO_BOARD = os.environ.get('TRELLO_TEST_BOARD')
    TRELLO_BOARD = "TEST_BOARD"


class SystemTestingConfig(Config):
    """Test configuration variables."""
    TESTING = True
    TRELLO_BOARD = "SYSTEM_TEST_BOARD"


config = {
    'system testing': SystemTestingConfig,
    'testing': TestingConfig,
    'default': Config
}
