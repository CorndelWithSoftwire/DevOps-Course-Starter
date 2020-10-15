class ViewModel(object):
    items = []

    def __init__(self, items):
        """
        docstring
        """
        self.items = items

    @property
    def todo_items(self):
        return self.items