"""Flask configuration class."""
import os

class Config:
    """Base configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    KEY = os.environ.get('KEY')
    TOKEN = os.environ.get('TOKEN')
    LIST_ID = os.environ.get('LIST_ID')
    DONE_LIST_ID = os.environ.get('DONE_LIST_ID')
    # if not SECRET_KEY:
    #     raise ValueError("No SECRET_KEY set for Flask application. Did you forget to run setup.sh?")
