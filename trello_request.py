from common import *

import os
import logging
import requests
from requests.exceptions import HTTPError


class TrelloRequest:
    BASE_PATH = "https://api.trello.com/1"
    APP_API_KEY = os.getenv("APP_API_KEY")
    APP_TOKEN = os.getenv("APP_TOKEN")

    logger = logging.getLogger('trello_request')

    def makeRequest(self, url, method, query_params=None, **kwargs):
        requestUrl = self.BASE_PATH + url
        self.logger.info(f"Trello {method} request {requestUrl} with queryParams: {query_params} and additional request: {kwargs}")

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

            self.logger.info(jsonResponse)

            return jsonResponse

        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Other error occurred: {err}')
        raise Exception("Request failed. See logs.")


class TrelloGetCards(TrelloRequest):
    URL_PATH = "/lists/{}/cards"

    def __init__(self, list_to_status_map):
        self._list_to_status_map = list_to_status_map

    def fetchForList(self, idList):
        url = self.URL_PATH.format(idList)
        return super().makeRequest(url, "GET")

    def fetchCard(self, id):
        url = "/card/{}".format(id)

        jsonData = super().makeRequest(url, "GET")

        return TodoItem(jsonData['name'], self._list_to_status_map[jsonData["idList"]], id)


class TrelloAddCard(TrelloRequest):
    URL_PATH = "/cards"

    def __init__(self, listId):
        self.listId = listId

    def add(self, item):
        url = self.URL_PATH

        query = {
            'idList': self.listId,
            'name': item.title
        }

        if item.duedate:
            query.update({"due": item.duedate})

        return super().makeRequest(url, "POST", query)


class TrelloUpdateCard(TrelloRequest):
    URL_PATH = "/cards/{}"

    def update(self, item, listId):
        url = self.URL_PATH.format(item.id)

        headers = {
            "Accept": "application/json"
        }

        query = {
            'name': item.title,
            'idList': listId
        }

        return super().makeRequest(url, "PUT", query, headers=headers)


class TrelloDeleteCard(TrelloRequest):
    URL_PATH = "/cards/{}"

    def delete(self, cardId):
        url = self.URL_PATH.format(cardId)
        return super().makeRequest(url, "DELETE")


class TrelloBoard(TrelloRequest):
    URL_BOARD_PATH = "/boards/{}"

    def fetchLists(self, id):
        url = self.URL_BOARD_PATH.format(id)

        json_data = super().makeRequest(url, "GET")

        return {x['name']: x['id'] for x in json_data}, {x['id']: x['name'] for x in json_data}
