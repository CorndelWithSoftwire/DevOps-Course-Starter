import os

import requests
from flask import Flask, render_template, request, redirect
from requests.exceptions import HTTPError

TODO_LIST_ID = os.getenv("TODO_LIST_ID")
DONE_LIST_ID = os.getenv("DONE_LIST_ID")


class TrelloRequest:
    BASE_PATH = "https://api.trello.com/1"
    APP_API_KEY = os.getenv("APP_API_KEY")
    APP_TOKEN = os.getenv("APP_TOKEN")

    def makeRequest(self, url, method, query_params=None, **kwargs):
        requestUrl = self.BASE_PATH + url
        print(f"Trello {method} request {requestUrl} with queryParams: {query_params} and additional request: {kwargs}")

        try:
            query = {
                'key': self.APP_API_KEY,
                'token': self.APP_TOKEN
            }

            if query_params:
                query.update(query_params)

            response = requests.request(
                method,
                requestUrl,
                params=query,
                **kwargs
            )

            response.raise_for_status()

            jsonResponse = response.json()

            print(jsonResponse)

            return jsonResponse

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        raise Exception("Request failed. See logs.")


class TrelloGetCards(TrelloRequest):
    URL_PATH = "/lists/{}/cards"

    def fetchForList(self, idList):
        url = self.URL_PATH.format(idList)
        return super().makeRequest(url, "GET")


class TrelloAddCard(TrelloRequest):
    URL_PATH = "/cards"

    def __init__(self, listId):
        self.listId = listId

    def add(self, name):
        url = self.URL_PATH

        query = {
            'idList': self.listId,
            'name': name
        }
        return super().makeRequest(url, "POST", query)


class TrelloUpdateCardStatus(TrelloRequest):
    URL_PATH = "/cards/{}"

    def update(self, cardId, status):
        url = self.URL_PATH.format(cardId)

        headers = {
            "Accept": "application/json"
        }

        query = {
            'idList': DONE_LIST_ID
        }
        return super().makeRequest(url, "PUT", query, headers=headers)


class TrelloDeleteCard(TrelloRequest):
    URL_PATH = "/cards/{}"

    def delete(self, cardId):
        url = self.URL_PATH.format(cardId)
        return super().makeRequest(url, "DELETE")


class TodoItem:
    def __init__(self, id, title, status):
        self.id = id
        self.title = title
        self.status = status


app = Flask(__name__, static_url_path='/static')
app.config.from_object('flask_config.Config')

trelloRequest = TrelloRequest()


@app.route('/')
def index():
    getTodoList = TrelloGetCards().fetchForList(TODO_LIST_ID)
    toDoItems = [TodoItem(x['id'], x['name'], 'Not Started') for x in getTodoList]

    getDoneList = TrelloGetCards().fetchForList(DONE_LIST_ID)
    doneItems = [TodoItem(x['id'], x['name'], 'Completed') for x in getDoneList]

    items = toDoItems + doneItems
    sorteditems = sorted(items, key=lambda item: item.status, reverse=True)
    return render_template('/index.html', items=sorteditems)


@app.route('/additem', methods=['POST'])
def additem():
    todoItemTitle = request.form.get('newitem')
    TrelloAddCard(TODO_LIST_ID).add(todoItemTitle)

    return redirect(request.referrer)


@app.route('/deleteitem/<id>', methods=['POST'])
def deleteitem(id):
    TrelloDeleteCard().delete(id)

    return redirect(request.referrer)


@app.route('/check/<id>', methods=['POST'])
def checkitem(id):
    TrelloUpdateCardStatus().update(id, 'Completed')

    return redirect(request.referrer)


if __name__ == '__main__':
    app.run()
