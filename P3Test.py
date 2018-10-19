import unittest
from Array_Deque import Array_Deque
from Linked_List_Deque import Linked_List_Deque
from Deque_Generator import get_deque

class Array_Deque_Tester(unittest.TestCase):

  def setUp(self):
    self.__deque = get_deque()
    
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
    self.assertEqual('[ ]', str(self.__deque))
    returned = self.__deque.peek_front()
    self.assertEqual(None, returned)
    
  def test_peek_front_one(self):
    self.__deque.push_front('Data')
    self.__deque.peek_front()
    self.assertEqual('[ Data ]', str(self.__deque))
    returned = self.__deque.peek_front()
    self.assertEqual('Data', returned)
    
  def test_peek_front_three(self):
    self.__deque.push_front('Rocks')
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.__deque.peek_front()
    self.assertEqual('[ Data, Structures, Rocks ]', str(self.__deque))
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
    self.assertEqual('[ ]', str(self.__deque))
    returned = self.__deque.peek_front()
    self.assertEqual(None, returned)
  
  def test_peek_back_one(self):
    self.__deque.push_front('Data')
    self.__deque.peek_back()
    self.assertEqual('[ Data ]', str(self.__deque))
    returned = self.__deque.peek_front()
    self.assertEqual('Data', returned)
    
  def test_peek_back_three(self):
    self.__deque.push_front('Structures')
    self.__deque.push_back('Rocks')
    self.__deque.push_front('Data')
    self.assertEqual('[ Data, Structures, Rocks ]', str(self.__deque))
    returned = self.__deque.peek_front()
    self.assertEqual('Data', returned)

if __name__ == '__main__':
  unittest.main()