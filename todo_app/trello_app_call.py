from turtle import dot
import dotenv
import requests
import dotenv
import os

url = "https://api.trello.com/1/members/me/boards"

env_file = dotenv.load_dotenv(".env")
print(os.getenv("Trello_API_KEY"))
querystring = {
"key":os.getenv("Trello_API_KEY"),
"token":os.getenv("Trello_API_TOKEN")

}

response = requests.request("GET", url, params=querystring)

print(response.text)