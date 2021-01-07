class ViewModel:
   def __init__(self, items):
        self._items = items

   @property
   def items(self): 
      return self._items

   @property
   def todo(self): 
      empty_list=[]
      for item in self._items:
          if item.status == "To Do":
            empty_list.append(item)
      return empty_list

   @property
   def doing(self): 
      pass

   @property
   def done(self): 
      pass