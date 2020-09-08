"""Flask configuration class."""
import os

class Config:
    """Base configuration variables."""
    APP_API_KEY = os.environ.get('APP_API_KEY')
    if not APP_API_KEY:
        raise ValueError("No APP_API_KEY set for Flask application. Did you forget to run setup.sh?")
    APP_TOKEN = os.environ.get('APP_TOKEN')
    if not APP_TOKEN:
        raise ValueError("No APP_TOKEN set for Flask application. Did you forget to run setup.sh?")
    TODO_BOARD_ID = os.environ.get('TODO_BOARD_ID')
    if not TODO_BOARD_ID:
        raise ValueError("No TODO_BOARD_ID set for Flask application. Did you forget to run setup.sh?")
    TODO_LIST_ID = os.environ.get('TODO_LIST_ID')
    if not TODO_LIST_ID:
        raise ValueError("No TODO_LIST_ID set for Flask application. Did you forget to run setup.sh?")
    DONE_LIST_ID = os.environ.get('DONE_LIST_ID')
    if not DONE_LIST_ID:
        raise ValueError("No DONE_LIST_ID set for Flask application. Did you forget to run setup.sh?")
