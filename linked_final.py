class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation
      self.val = val
      self.next = None
      self.previous = None
      
      

  def __init__(self): 
    ''' Create an empty list.'''
    self.__size = 0
    self.__header = Linked_List.__Node(None)
    self.__trailer = Linked_List.__Node(None)
    self.__header.next = self.__trailer
    self.__trailer.previous = self.__header
    
    
    
    #self.__head = Linked_List.__Node(val)
    #self.__tail = Linked_List.__Node(val) # may not need to be here
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    # TODO replace pass with your implementation
    return self.__size
      
  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
    
    newest = self.__Node(val)
    newest.next = self.__trailer
    current = self.__trailer.previous
    current.next = newest
    self.__trailer.previous = newest
    newest.previous = current
    self.__size += 1    

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    # TODO replace pass with your implementation
    
    # Current pointer needs to be one less than where you want to index
    if index >= self.__size:
      raise IndexError   
    newest = self.__Node(val)
    current = self.__header #WHY?
    for i in range(0,index):
      current = current.next   
    newest.next = current.next
    newest.previous = current
    current.next = newest
    newest.next.previous = newest
    self.__size += 1

    
    

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
    if index >= self.__size:
      raise IndexError
    current = self.__header
    for i in range(0, index):
      current = current.next
    temp = current.next.val
    current.next = current.next.next
    current.next.previous = current
    self.__size -= 1
    return temp
      # Will the garbage collector get the original current.next?
      

  def get_element_at(self, index):
    if index >= self.__size:
      raise IndexError
    current= self.__header
    for i in range(0, index + 1):#Check this syntax
      current = current.next
    return current.val
    
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node 
    # at the specified index, but do not unlink it from 
    # the list. If the specified index is invalid, raise 
    # an IndexError exception.
    # TODO replace pass with your implementation
    

  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.
    
    # Get rid of head with a temporary value and move the index over to the left.
    if self.__size == 0:
      return
    current = self.__header.next
    temp = current
    self.__header.next = current.next
    current.next.previous = self.__header
    
    # Link Temp in first. Put head at the tail
    temp.next = self.__trailer
    temp.previous = self.__trailer.previous
    self.__trailer.previous.next = temp
    self.__trailer.previous = temp
    
    
  def __str__(self):
    
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
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
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    self.__iter_index = 0
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation
    if self.__iter_index == self.__size:
      raise StopIteration
    to_return = self.get_element_at(self.__iter_index)  # something
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
  print(ll)

  
  
