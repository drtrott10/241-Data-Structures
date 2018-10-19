class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      self.val = val
      self.next = None
      self.previous = None

  def __init__(self): 
    self.__size = 0
    self.__header = Linked_List.__Node(None)
    self.__trailer = Linked_List.__Node(None)
    self.__header.next = self.__trailer
    self.__trailer.previous = self.__header

  def __len__(self):
    return self.__size
      
  def append_element(self, val):
    newest = self.__Node(val)
    newest.next = self.__trailer
    current = self.__trailer.previous
    current.next = newest
    self.__trailer.previous = newest
    newest.previous = current
    self.__size += 1    

  def insert_element_at(self, val, index):
    if self.__size == 0:
      raise IndexError
    if self.__size == 1 and index != 0:
      raise IndexError
    if self.__size > 1 and index not in range (0,self.__size):
      raise IndexError  
    newest = self.__Node(val)
    current = self.__header
    for i in range(0,index):
      current = current.next   
    newest.next = current.next
    newest.previous = current
    current.next = newest
    newest.next.previous = newest
    self.__size += 1

  def remove_element_at(self, index):
    if index >= self.__size or index < 0:
      raise IndexError
    current = self.__header
    for i in range(0, index):
      current = current.next
    temp = current.next.val
    current.next = current.next.next
    current.next.previous = current
    self.__size -= 1
    return temp      

  def get_element_at(self, index):
    if index >= self.__size or index < 0:
      raise IndexError
    current= self.__header
    for i in range(0, index + 1):
      current = current.next
    return current.val    

  def rotate_left(self):
    if self.__size == 0:
      return
    current = self.__header.next
    temp = current
    self.__header.next = current.next
    current.next.previous = self.__header
    temp.next = self.__trailer
    temp.previous = self.__trailer.previous
    self.__trailer.previous.next = temp
    self.__trailer.previous = temp
    
  def __str__(self):
    ll = '[ '
    if self.__size == 0:
      return '[ ]'
    current= self.__header.next
    if self.__size == 1:
      ll += str(current.val) + ' ]'
      return ll
    else:
      while current.next != self.__trailer:
        ll += str(current.val) + ', ' 
        current = current.next
      return ll + str(current.val) + ' ]'
      
  def __iter__(self):
    self.__iter_index = 0
    return self

  def __next__(self):
    if self.__iter_index == self.__size:
      raise StopIteration
    to_return = self.get_element_at(self.__iter_index)
    self.__iter_index += 1
    return to_return
    

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests
  ll = Linked_List()
  print(ll)
  ll.append_element(1)
  print(ll)
  try:
    ll.get_element_at(0)
  except IndexError:
    print('Error, index out of range')
  print(ll)
  try:
    ll.remove_element_at(3)
  except IndexError:
    print('Error, index out of range')
  print(ll)
  try:
    ll.insert_element_at(3,3)
  except IndexError:
    print('Error, index out of range')
  print(ll)
  
#APPEND
  ll.append_element(5)
  ll.append_element(3)
  ll.append_element(21)
  print(len(ll))
  print(ll)
#ROTATE LEFT
  ll.rotate_left()
  print(ll)
  ll.rotate_left()
  print(ll)
  ll.rotate_left()
  print(ll)
#REMOVE
  ll.remove_element_at(2)
  print(ll)
#INSERT
  ll.insert_element_at(7,1)
  print(ll)
  for item in ll:
      print(item)
  try:
    ll.insert_element_at(2,10)
  except IndexError:
    print('Error, index out of range')
  print(ll)
  ll.append_element(6)
  ll.append_element(4)
  ll.append_element(10)
  ll.append_element(11)
  print(ll)
  ll.rotate_left()
  
  ll.insert_element_at(4,-10)
  
  print(ll)