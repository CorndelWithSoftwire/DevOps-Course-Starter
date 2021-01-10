
from datetime import datetime


class Card:
    """
    card class for processing contents of API
    Returns:
        Card class object
    """

    def __init__(self, Lists, i):
        self.id = i["id"]
        self.name = i["name"]
        self.listId = i["idList"]
        self.desc = i["desc"]
        self.creationTime = datetime.fromtimestamp(int(i["id"][0:8], 16))
        try:
            self.due = datetime.strftime(datetime.fromisoformat(
                i["due"].replace('Z', '+00:00')), "%Y-%m-%d")
        except:
            self.due = ""

        self.listName = [l.name for l in Lists if l.id == i["idList"]][0]
        self.orderBy = [l.orderBy for l in Lists if l.id == i["idList"]][0]

        try:
            self.dateLastActivity = datetime.strftime(datetime.fromisoformat(
                i["dateLastActivity"].replace('Z', '+00:00')), "%Y-%m-%d")
        except:
            self.dateLastActivity = ""

    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
            'listId': self.listId,
            'listName': self.listName,
            'desc': self.desc,
            'creationTime': self.creationTime,
            'due': self.due,
            'dateLastActivity': self.dateLastActivity,
            'orderBy': self.orderBy
        }

    def __str__(self):
        return "Card(id="+self.id+", name="+self.name+")"


class List:
    """
    list class for processing contents of the API
    Return:
        List class object
    """

    def __init__(self, l, i):
        self.id = l["id"]
        self.name = l["name"]
        self.orderBy = i

    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
            'orderBy': self.orderBy
        }

    def __str__(self):
        return "List(id="+self.id+", name="+self.name+", orderBy:"+self.orderBy+")"


class ViewModel:

    def __init__(self, cards, lists):
        self._cards = cards
        self._lists = lists

    def get_date(self):
        return datetime.date(datetime.today()).strftime("%Y-%m-%d")

    @property
    def cards(self):
        return self._cards

    @property
    def lists(self):
        return self._lists

    @property
    def show_all_done_items(self):
        if len([i for i in self._cards if i.listName == "DONE"]) > 5:
            return False
        return True

    @property
    def recent_done_items(self):
        return [i for i in self._cards if i.listName == "DONE" and i.dateLastActivity == self.get_date()]

    @property
    def older_done_items(self):
        return [i for i in self._cards if i.listName == "DONE" and i.dateLastActivity != self.get_date()]
