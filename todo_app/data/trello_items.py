from flask import Flask, render_template, request

import requests
import os

def get_trello_cards():
    url = f'https://api.trello.com/1/boards/{os.getenv("TRELLO_BOARD_ID")}/lists'

    print(os.getenv("API_KEY"))

    querystring = {
        "key": os.getenv("API_KEY"),
        "token": os.getenv("API_TOKEN"),
        "cards": "open"
    }

    response = requests.get(url, params=querystring)
    response_json = response.json()
    return response_json

def create_todo():
    url = "https://api.trello.com/1/cards"
    new_todo_title = request.form['todo-name']
    querystring = {
        "key":os.getenv("API_KEY"),
        "token":os.getenv("API_TOKEN"),
        "idList":os.getenv("TRELLO_TODO_LIST_ID"),
        "name": new_todo_title
    }
    response = requests.request("POST", url, params=querystring)
    response.raise_for_status()

def change_status():
    card_id = request.form['todo-id']  
    url = f"https://api.trello.com/1/cards/{card_id}"
    querystring = {
            "key":os.getenv("API_KEY"),
            "token":os.getenv("API_TOKEN"),
            "idList":os.getenv("TRELLO_DONE_LIST_ID")
        }

    response = requests.request("PUT", url, params=querystring)