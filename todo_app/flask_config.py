"""Flask configuration class."""
import os


class Config:
    """Base configuration variables."""
    def __init__(self):
        self.MONGO_URL = os.environ.get('MONGO_URL')
        self.MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')
        self.MONGO_LIST_COLLECTION = os.environ.get('MONGO_LIST_COLLECTION')
        if not self.MONGO_URL:
            raise ValueError("No SECRET_KEY set for Flask application. Did you forget to run setup.sh?")
