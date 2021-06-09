import os
from dotenv import find_dotenv, load_dotenv

file_path = find_dotenv('.env')
load_dotenv(file_path, override=True)

class Config:
    MONGO_CONNECTION = os.environ.get("MONGO_CONNECTION")
    if not MONGO_CONNECTION:
        raise ValueError("Mongo Connection string does not exist")
    MONGO_DB = os.environ.get("MONGO_DB")
    if not MONGO_DB:
        raise ValueError("Mongo DB is not expected value")