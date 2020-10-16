class ViewModel(object):
    items = []

    def __init__(self, items):
        """
        docstring
        """
        self.items = items

    @property
    def todo_items(self):
        return list(filter(containsToDo, self.items))

    @property
    def all_items(self):
        return list(filter(containsToDo, self.items))


def containsToDo(element):
    if type(element).__name__ == 'Item':
        return element.status == "To Do"
    else:
        return False