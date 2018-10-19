import unittest
from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
    
  def setUp(self):
    # Run your tests with each deque type to ensure that
    # they behave identically.
    self.__deque = get_deque(ARR_DEQUE_TYPE)
    self.__stack = Stack()
    self.__queue = Queue()
    
  def test_empty_str(self):
     self.assertEqual('[ ]', str(self.__deque), 'Empty deque should print as "[ ]"')
     
  def test_push_front_empty(self):
    self.__deque.push_front('Data')
    self.assertEqual('[ Data ]', str(self.__deque))
  
  def test_push_front_one(self):
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.assertEqual('[ Data, Structures ]', str(self.__deque))
  
  def test_push_front_three(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.assertEqual('[ Data, Structures, Rocks ]', str(self.__deque))
  
  def test_pop_front_empty(self):
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))
    self.assertEqual('[ ]', str(self.__deque))
  
  def test_pop_front_one(self):
    self.__deque.push_front('Data')
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))
    
  def test_pop_front_three(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.assertEqual('[ Rocks ]', str(self.__deque))

  def test_peek_front_empty(self):
    self.__deque.peek_front()
    returned = self.__deque.peek_front()
    self.assertEqual(None, returned)
    
  def test_peek_front_one(self):
    self.__deque.push_front('Data')
    self.__deque.peek_front()
    returned = self.__deque.peek_front()
    self.assertEqual('Data', returned)
    
  def test_peek_front_three(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.__deque.peek_front()
    returned = self.__deque.peek_front()
    self.assertEqual('Data', returned)
    
  def test_push_back_empty(self):
    self.__deque.push_back('Data')
    self.assertEqual('[ Data ]', str(self.__deque))
  
  def test_push_back_one(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    self.assertEqual('[ Data, Structures ]', str(self.__deque))
    
  def test_push_back_three(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    self.__deque.push_back('Rocks')
    self.assertEqual('[ Data, Structures, Rocks ]', str(self.__deque))
    
  def test_pop_back_empty(self):
    self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))
    self.assertEqual('[ ]', str(self.__deque))
 
  def test_pop_back_one_with_push_back(self):
    self.__deque.push_back('Data')
    self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))
    self.assertEqual('[ ]', str(self.__deque))
    
  
  def test_pop_back_one_with_push_front(self):
    self.__deque.push_front('Data')
    self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))
    self.assertEqual('[ ]', str(self.__deque))
    
  def test_pop_back_three(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    self.__deque.push_back('Rocks')
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.assertEqual(1, len(self.__deque))
    self.assertEqual('[ Data ]', str(self.__deque))
    
  def test_pop_back_three_with_push_front (self):
    self.__deque.push_front('Structures')
    self.__deque.push_back('Rocks')
    self.__deque.push_front('Data')
    self.__deque.pop_back()
    self.assertEqual(2, len(self.__deque))
    self.assertEqual('[ Data, Structures ]', str(self.__deque))

    
  def test_peek_back_empty(self):
    self.__deque.peek_back()
    returned = self.__deque.peek_front()
    self.assertEqual(None, returned)
  
  def test_peek_back_one(self):
    self.__deque.push_back('Data')
    self.__deque.peek_back()
    returned = self.__deque.peek_back()
    self.assertEqual('Data', returned)
    
  def test_peek_back_three(self):
    self.__deque.push_front('Structures')
    self.__deque.push_back('Rocks')
    self.__deque.push_front('Data')
    returned = self.__deque.peek_back()
    self.assertEqual('Rocks', returned)

  def test_Stack_push_empty(self):
    self.__stack.push('Data')
    self.assertEqual('[ Data ]', str(self.__stack))
    
  def test_Stack_push_one(self):
    self.__stack.push('Structures')
    self.__stack.push('Data')
    self.assertEqual('[ Data, Structures ]', str(self.__stack))
    
  def test_Stack_push_three(self):
    self.__stack.push('Rocks')
    self.__stack.push('Structures')
    self.__stack.push('Data')
    self.assertEqual('[ Data, Structures, Rocks ]', str(self.__stack))
    
  def test_Stack_peek_empty(self):
    self.__stack.peek()
    returned = self.__stack.peek()
    self.assertEqual(None, returned)
    
  def test_Stack_peek_one(self):
    self.__stack.push('Data')
    self.__stack.peek()
    returned = self.__stack.peek()
    self.assertEqual('Data', returned)
    
  def test_Stack_peek_three(self):
    self.__stack.push('Rocks')
    self.__stack.push('Structures')
    self.__stack.push('Data')
    self.__stack.peek()
    returned = self.__stack.peek()
    self.assertEqual('Data', returned)
    
  def test_Stack_pop_empty(self):
    self.__stack.pop()
    returned = self.__stack.peek()
    self.assertEqual(None, returned)
    
  def test_Stack_pop_one(self):
    self.__stack.push('Data')    
    returned = self.__stack.pop()
    self.assertEqual('Data', returned)
    
  def test_Stack_pop_three(self):
    self.__stack.push('Rocks')
    self.__stack.push('Structures')
    self.__stack.push('Data')
    returned = self.__stack.pop()
    self.assertEqual('Data', returned)
    
  def test_Queue_enqueue_empty(self):
    self.__queue.enqueue('Data')
    self.assertEqual('[ Data ]', str(self.__queue))
    
  def test_Queue_enqueue_one(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.assertEqual('[ Structures, Data ]', str(self.__queue))
    
  def test_Queue_enqueue_three(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.__queue.enqueue('Rocks')
    self.assertEqual('[ Rocks, Structures, Data ]', str(self.__queue))
    
  def test_Queue_dequeue_empty(self):
    self.__queue.dequeue()
    returned = self.__queue.dequeue()
    self.assertEqual(None, returned)
  
  def test_Queue_dequeue_one(self):
    self.__queue.enqueue('Data')  
    returned = self.__queue.dequeue()
    self.assertEqual('Data', returned)
    
  def test_Queue_dequeue_three(self):
    self.__queue.enqueue('Data') 
    self.__queue.enqueue('Structures')
    self.__queue.enqueue('Rocks')
    returned = self.__queue.dequeue()
    self.assertEqual('Data', returned)
    
    


    

    

    
    
    


    
  
    
    
    
    
  
    
  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_

if __name__ == '__main__':
  unittest.main()

