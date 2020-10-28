import os
from dotenv import load_dotenv, find_dotenv
from app import create_app

import logging

# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))
ENV_FULL_PATH = os.path.join(BASEDIR, '.env')
print(ENV_FULL_PATH)

# Connect the path with your '.env' file name
load_dotenv(ENV_FULL_PATH)

test_var = os.getenv("APP_API_KEY")
print(test_var)

if __name__ == "__main__":
    print("Running application")
    application = create_app()
    application.run()

