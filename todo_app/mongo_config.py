import os
from dotenv import find_dotenv, load_dotenv

file_path = find_dotenv('.env')
load_dotenv(file_path, override=True)

class Config:
    MONGO_USER = os.environ.get("MONGO_USER")
    if not MONGO_USER:
        raise ValueError("Mongo DB Username is not expected value")
    MONGO_PASS = os.environ.get("MONGO_PASS")
    if not MONGO_PASS:
        raise ValueError("Mongo DB Password is not expected value")
    MONGO_URL = os.environ.get("MONGO_URL")
    if not MONGO_URL:
        raise ValueError("Mongo DB URL is not expected value")
    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME")
    if not MONGO_DB_NAME:
        raise ValueError("Mongo DB Name is not expected value")