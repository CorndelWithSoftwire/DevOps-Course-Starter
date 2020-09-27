import requests
from requests import Response

from flask_config import Config


def create_board(name) -> Response:
    """
    Create a new board in trello.

    Returns:
        list: The list of saved items.
    """
    url = "https://api.trello.com/1/boards/"

    query = {
        'key': Config.KEY,
        'token': Config.TOKEN,
        'name': name
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )

    print(response)
    return response


def delete_board(board_id):
    url = f'https://api.trello.com/1/boards/{board_id}'
    query = {
        'key': Config.KEY,
        'token': Config.TOKEN,
    }
    response = requests.request(
        "DELETE",
        url,
        params=query
    )

    print(response.text)
    return response


def get_lists_in_board(boardid) -> Response:
    url = f"https://api.trello.com/1/boards/{boardid}/lists"

    query = {
        'key': Config.KEY,
        'token': Config.TOKEN,
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )

    print(response.text)
    return response


class TrelloBoard:
    def __init__(self, response) -> None:
        self._response = response

    def get_lists(self):
        return self._response

    def list_id(self, name):
        todo_list = list(filter(lambda item: item['name'] == name, self._response))
        return todo_list[0]['id']