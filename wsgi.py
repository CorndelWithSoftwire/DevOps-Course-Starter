import os
from dotenv import load_dotenv, find_dotenv
from app import create_app

load_dotenv(find_dotenv())

test_var = os.getenv("APP_API_KEY")
print(test_var)

if __name__ == "__main__":
    print("Running application")
    some_app = create_app()
    some_app.run()

