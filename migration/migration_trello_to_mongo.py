# Migration script - from trello to mongo
# get data from trello collection
# insert into mongo db - if it hasnt already been inserted
import os

# Trello
import jsons
from dotenv import load_dotenv, find_dotenv

from migration.trello_request import *
from todoapp.common import Lists
from todoapp.mongo_database import MongoDatabase

# Connect the path with your '.env' file name
file_path = find_dotenv('.env.migration')
load_dotenv(file_path, override=True)

APP_API_KEY = os.getenv("APP_API_KEY")
APP_TOKEN = os.getenv("APP_TOKEN")
TODO_BOARD_ID = os.getenv("TODO_BOARD_ID")

# MONGO
DB_URL = os.getenv("DB_URL")

TrelloRequest.APP_TOKEN = APP_TOKEN
TrelloRequest.APP_API_KEY = APP_API_KEY
MongoDatabase.DB_URL = DB_URL


def fetch_trello_board_lists():
    todo_lists_by_name, todo_lists_by_id = TrelloBoard().fetchLists(TODO_BOARD_ID)
    todo_list_id = todo_lists_by_name[Lists.TODO_LIST_NAME]
    done_list_id = todo_lists_by_name[Lists.DONE_LIST_NAME]
    return Lists(todo_list_id, done_list_id)


def createTrelloListWithStatus(status, itemList):
    return [TodoItem(x['name'], status, x['id'], duedate=x['due'], last_modified=x['dateLastActivity']) for x in
            itemList]


board_lists = fetch_trello_board_lists()

trello_get_cards = TrelloGetCards(board_lists.list_to_status_map)

get_todo_list = trello_get_cards.fetchForList(board_lists.todo_list_id)
to_do_items = createTrelloListWithStatus(NOT_STARTED, get_todo_list)

get_done_list = trello_get_cards.fetchForList(board_lists.done_list_id)
done_items = createTrelloListWithStatus(COMPLETED, get_done_list)

mongoDatabase = MongoDatabase().getDatabase()

for item in to_do_items:
    mongoDatabase[Lists.TODO_LIST_NAME].update_one({ "title": item.title}, {'$set': jsons.dump(item)}, upsert=True)

for item in done_items:
    mongoDatabase[Lists.DONE_LIST_NAME].update_one({ "title": item.title}, {'$set': jsons.dump(item)}, upsert=True)

print(f"Migration complete. Migrated counts todo[{len(get_todo_list)}] done[{len(get_done_list)}]")