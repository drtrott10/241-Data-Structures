from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE

class Stack:

  def __init__(self):
    self.__contents = get_deque()
    self.__size = 0
    
    
    # TODO replace pass with your implementation.
    

  def __str__(self):
    return (str(self.__contents))
    # TODO replace pass with your implementation.

  def __len__(self):
    return self.__size 
    # TODO replace pass with your implementation.

  def push(self, val):
    self.__contents.push_front(val)
    self.__size += 1
    # TODO replace pass with your implementation.

  def pop(self):
    returned = self.__contents.pop_front() 
    self.__size -= 1
    return returned

    # TODO replace pass with your implementation.

  def peek(self):
    returned = self.__contents.peek_front()
    return returned 
    
    # TODO replace pass with your implementation.

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#pass
