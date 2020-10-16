class ViewModel(object):
    items = []

    def __init__(self, items):
        """
        docstring
        """
        self.items = items

    @property
    def todo_items(self):
        return list(filter(lambda item: containsStatus(item, "To Do"), self.items))

    @property
    def all_items(self):
        return self.items

    @property
    def doing_items(self):
        return list(filter(lambda item: containsStatus(item, "Doing"), self.items))


def containsStatus(element, status):
    if type(element).__name__ == 'Item':
        return element.status == status
    else:
        return False