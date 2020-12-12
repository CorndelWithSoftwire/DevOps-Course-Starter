import os

class Config:
    """Base configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TRELLO_KEY = os.environ.get('TRELLO_KEY')
    TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
    TRELLO_BOARD = os.environ.get('TRELLO_BOARD')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")

    if not TRELLO_KEY:
        raise ValueError("No TRELLO_KEY set for Flask application. Please set this value in .env")

    if not TRELLO_TOKEN:
        raise ValueError("No TRELLO_TOKEN set for Flask application. Please set this value in .env")

    if not TRELLO_BOARD:
        raise ValueError("No TRELLO_BOARD set for Flask application. Please set this value in .env")