import logging
import os

from dotenv import load_dotenv

from todoapp.app import create_app

logging.basicConfig(level=logging.DEBUG)

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))
ENV_FULL_PATH = os.path.join(BASEDIR, '../.env')
print(f"ENV_FULL_PATH: {ENV_FULL_PATH}")

# Connect the path with your '.env' file name
load_dotenv(ENV_FULL_PATH)

if __name__ == "__main__":
    print("Running application")
    application = create_app()
    application.run()
