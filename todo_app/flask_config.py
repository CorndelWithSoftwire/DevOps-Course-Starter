"""Flask configuration class."""
import os

class Config:
    """Base configuration variables."""
    # Uses a default if nothing in environment
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sdfdsfsdf332lklkmsdcmclmclsdkmcdsokm')
