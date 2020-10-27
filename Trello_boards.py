import requests
from Trello_items import boardsurl, get_trello_key, get_trello_token, build_auth_query
from dotenv import load_dotenv, find_dotenv


def create_trello_board():
    """
    Adds a new board in Trello with the given name

    Args:
        title: The name of the Board.

    Returns:
        item: The saved item.
    """
    query = build_auth_query()
    query['name'] = "Test_Board"
    response = requests.post(boardsurl, params=query)
    response_json = response.json()
    return response_json['id']

def delete_trello_board(id):
    """
    deletes the board in Trello with the given id

    Args:
        id: The id of the Board.

    Returns:
        : 
    """
    idboardurl = boardsurl + id
    requests.delete(idboardurl, params=build_auth_query())
    return 
    