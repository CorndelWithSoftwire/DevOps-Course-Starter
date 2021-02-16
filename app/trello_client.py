from datetime import datetime
import requests
import json
from app.to_do_item import ToDoItem
from app.flask_config import Config


class TrelloClient:
    
    def __init__(self):
        self.config: Config = Config()
        self.base_request_url = 'https://api.trello.com/1/boards/'+self.config.boardId+'/'
        self.request_credentials = f'?key={self.config.key}&token={self.config.token}'

    def get_items(self) -> list:
        """
        Fetches all saved items from the trello api.

        Returns:
            list: The list of items.
        """
        
        cards_request = requests.get(self.base_request_url+'cards'+self.request_credentials)

        cards_json = json.loads(cards_request.content)
        list_id_dict = self.get_lists()

        items = []
        for node in cards_json:
            date_in_datetime = datetime.strptime(node['dateLastActivity'], '%Y-%m-%dT%H:%M:%S.%fZ')
            items.append(ToDoItem(node['id'], list_id_dict[node['idList']], node['name'], date_in_datetime))  
        
        return items

    def get_item(self, id) -> dict:
        """
        Fetches the saved item with the specified ID.

        Args:
            id: The ID of the item.

        Returns:
            item: The saved item, or None if no items match the specified ID.
        """
        items = TrelloClient.get_lists()
        return next((item for item in items if item['id'] == int(id)), None)


    def add_item(self, title):
        """
        Adds a new item with the specified title to the board.

        Args:
            title: The title of the item.
        """

        json_list = self.get_lists()

        todo_list = ''
        for key, value in json_list.items():
            if value == 'To Do':
                todo_list = key

        url = 'https://api.trello.com/1/cards'+self.request_credentials+'&idList='+todo_list+'&name='+title

        response = requests.post(url)
        print(response.text)


    def mark_complete(self, id):
        """
        Marks an item as complete

        Args:
            item: The item to save.
        """
        json_list = self.get_lists()

        todo_list = ''
        completed_list = ''

        for key, value in json_list.items():
            if value == 'To Do':
                todo_list = key
            elif value == 'Done':
                completed_list = key    

        url = 'https://api.trello.com/1/cards/'+id+self.request_credentials+'&idList='+completed_list

        requests.put(url)


    def delete_item_by_id(self, id) -> None:
        """
        Deletes the item provided. Does nothing if the item does not exist.

        Args:
            item: The item to delete.
        """
        url = 'https://api.trello.com/1/cards/'+id+self.request_credentials

        response = requests.delete(url)

        print(response.text)

    def get_lists(self) -> dict:
        json_response = json.loads(requests.get(self.base_request_url+'lists'+self.request_credentials).content)
        board_id_dict = {}
        for node in json_response:
            board_id_dict[node['id']] = node['name']
        return board_id_dict    
