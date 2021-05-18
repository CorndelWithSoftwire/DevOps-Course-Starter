"""Flask configuration class."""
import os


class Config:
    """Base configuration variables."""
    DB_URL = os.environ.get('DB_URL')
    if not DB_URL:
        raise ValueError(f"No DB_URL set for Flask application or corrupt: [{DB_URL}] ?")
