from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import requests
from requests.exceptions import HTTPError
import os

TODO_LIST_ID = os.getenv("TODO_LIST_ID")
DONE_LIST_ID = os.getenv("DONE_LIST_ID")


class TrelloRequest:
    BASE_PATH = "https://api.trello.com/1"
    APP_API_KEY = os.getenv("APP_API_KEY")
    APP_TOKEN = os.getenv("APP_TOKEN")

    # def __init__(self):

    def makeRequest(self, url, resourceId, method="GET", payload=None):
        try:
            tokenParams = {
                'key': self.APP_API_KEY,
                'token': self.APP_TOKEN
            }

            response = requests.request(
                method,
                self.BASE_PATH % url.format(resourceId),
                params=tokenParams.update(payload)
            )

            response.raise_for_status()

            jsonResponse = response.json()

            print(jsonResponse)

            return jsonResponse

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        # raise Exception("Request processing failed!")


class TrelloGetCards:
    BASE_PATH = "https://api.trello.com/1"
    APP_API_KEY = os.getenv("APP_API_KEY")
    APP_TOKEN = os.getenv("APP_TOKEN")

    URL_PATH = "/lists/{}/cards"

    def makeRequest(self, idList):
        url = self.BASE_PATH + self.URL_PATH.format(idList)
        print(f"Trello request {url}")

        try:
            query = {
                'key': self.APP_API_KEY,
                'token': self.APP_TOKEN
            }

            response = requests.request(
                "GET",
                url,
                params=query
            )

            response.raise_for_status()

            jsonResponse = response.json()

            print(jsonResponse)

            return jsonResponse

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')


class TrelloAddCard:
    BASE_PATH = "https://api.trello.com/1"
    APP_API_KEY = os.getenv("APP_API_KEY")
    APP_TOKEN = os.getenv("APP_TOKEN")

    URL_PATH = "/cards"

    def makeRequest(self, name):
        url = self.BASE_PATH + self.URL_PATH
        print(f"Trello request {url}")

        try:
            query = {
                'key': self.APP_API_KEY,
                'token': self.APP_TOKEN,
                'idList': TODO_LIST_ID,
                'name': name
            }

            response = requests.request(
                "POST",
                url,
                params=query
            )

            response.raise_for_status()

            jsonResponse = response.json()

            print(jsonResponse)

            return jsonResponse

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')


class TrelloUpdateCardStatus:
    BASE_PATH = "https://api.trello.com/1"
    APP_API_KEY = os.getenv("APP_API_KEY")
    APP_TOKEN = os.getenv("APP_TOKEN")

    URL_PATH = "/cards/{}"

    def makeRequest(self, cardId, status):
        url = self.BASE_PATH + self.URL_PATH.format(cardId)
        print(f"Trello request {url}")

        try:

            headers = {
                "Accept": "application/json"
            }

            query = {
                'key': self.APP_API_KEY,
                'token': self.APP_TOKEN,
                'idList': DONE_LIST_ID
            }

            # ,'idLabels': status

            response = requests.request(
                "PUT",
                url,
                headers=headers,
                params=query
            )

            response.raise_for_status()

            jsonResponse = response.json()

            print(jsonResponse)

            return jsonResponse

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')


class TrelloDeleteCard:
    BASE_PATH = "https://api.trello.com/1"
    APP_API_KEY = os.getenv("APP_API_KEY")
    APP_TOKEN = os.getenv("APP_TOKEN")

    TODO_LIST_ID = os.getenv("TODO_LIST_ID")
    DONE_LIST_ID = os.getenv("DONE_LIST_ID")
    URL_PATH = "/cards/{}"

    def makeRequest(self, cardId):
        url = self.BASE_PATH + self.URL_PATH.format(cardId)
        print(f"Trello request {url}")

        try:
            query = {
                'key': self.APP_API_KEY,
                'token': self.APP_TOKEN,
                'idList': DONE_LIST_ID
            }

            response = requests.request(
                "DELETE",
                url,
                params=query
            )

            response.raise_for_status()

            jsonResponse = response.json()

            print(jsonResponse)

            return jsonResponse

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')


app = Flask(__name__, static_url_path='/static')
app.config.from_object('flask_config.Config')

trelloRequest = TrelloRequest()


@app.route('/')
def index():
    getTodoList = TrelloGetCards().makeRequest(TODO_LIST_ID)
    toDoItems = [{'id': x['id'], 'title': x['name'], 'status': 'Not Started'} for x in getTodoList]

    getDoneList = TrelloGetCards().makeRequest(DONE_LIST_ID)
    doneItems = [{'id': x['id'], 'title': x['name'], 'status': 'Completed'} for x in getDoneList]

    items = toDoItems + doneItems
    sorteditems = sorted(items, key=lambda item: item['status'], reverse=True)
    return render_template('/index.html', items=sorteditems)


@app.route('/additem', methods=['POST'])
def additem():
    todoItemTitle = request.form.get('newitem')
    TrelloAddCard().makeRequest(todoItemTitle)

    return redirect(request.referrer)


@app.route('/deleteitem/<id>', methods=['POST'])
def deleteitem(id):
    TrelloDeleteCard().makeRequest(id)

    return redirect(request.referrer)


@app.route('/check/<id>', methods=['POST'])
def checkitem(id):
    TrelloUpdateCardStatus().makeRequest(id, 'Completed')

    return redirect(request.referrer)


if __name__ == '__main__':
    app.run()
