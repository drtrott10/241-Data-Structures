from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__size = 0
    self.__frontpointer = 0
    self.__backpointer = 0
    # TODO replace pass with any additional initializations you need.

  def __str__(self):
    arr = '[ '
    if self.__size == 0:
      return '[ ]'
    current = self.__contents[0]
    if self.__size == 1:
      arr += str(current) + ' ]'
      return arr
    else:
      for i in range(0,self.__size-1,1):
        arr += str(self.__contents[i]) + ', ' 
      return arr + str(self.__contents[self.__size-1]) + ' ]'
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
  def __len__(self):
      return self.__size
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    

  def __grow(self):
      if self.__size == self.__capacity:
         self.__capacity *= 2
         temp = [None] * self.__capacity
         for i in range(len(self.__contents)):
              temp[i] = self.__contents[(self.__frontpointer + i )% len(self.__contents)]
         self.__contents = temp
         self.__frontpointer = 0
         self.__backpointer = self.__size -1
      else:
          return
          
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    
  def push_front(self, val):
    self.__grow() 
    for i in range(self.__size,0,-1):
        self.__contents[i]=self.__contents[i-1]
    self.__contents[0]= val
    self.__size += 1
        
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    
    
  def pop_front(self):
    if self.__size == 0:
      return None #cannot return array type
    else:
      temp = self.__contents[0]
      self.__contents[0] = None
      for i in range(0,self.__size-1):
        self.__contents[i]=self.__contents[i+1]
      self.__contents[self.__size-1] = None
      self.__size -= 1
      return temp
    
    # TODO replace pass with your implementation. Do not reduce the capacity.
    
    
  def peek_front(self):
    if self.__size==0:
      return None
    else:
      return self.__contents[0]
     
    # TODO replace pass with your implementation.
    
    
  def push_back(self, val):
    self.__grow()
    self.__contents[self.__size] = val
    self.__size += 1
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.

  
  def pop_back(self):
    if self.__size == 0:
      return None
    else:
      temp = self.__contents[self.__size-1]
      self.__contents[self.__size-1] = None
      self.__size -= 1
      return temp
      
        
    # TODO replace pass with your implementation. Do not reduce the capacity.

  def peek_back(self):
    if self.__size==0:
      return None
    else:
      return self.__contents[self.__size-1]
    # TODO replace pass with your implementation.

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass