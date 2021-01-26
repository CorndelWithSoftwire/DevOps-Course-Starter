class ViewModel:
   def __init__(self, items, todo, doing, done):
        self._items = items
        self._todo = todo
        self._doing = doing
        self._done = done

   @property
   def items(self): 
      return self._items

   @property
   def todo(self): 
      todo_list=[]
      for item in self._items:
          if item.status == "To Do":
            todo_list.append(item)
      return todo_list

   @property
   def doing(self): 
      doing_list=[]
      for item in self._items:
          if item.status == "Doing":
            doing_list.append(item)
      return doing_list

   @property
   def done(self): 
      done_list=[]
      for item in self._items:
          if item.status == "Done":
            done_list.append(item)
      return done_list