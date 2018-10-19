import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  open_delimiters= ['(', '[', '{']
  closed_delimiters= [')', '}', ']']
  Stack1 = Stack() 
  file = open(filename,'r')
  for line in file:
    for char in line:
      if(char in open_delimiters):
        Stack1.push(char)
      elif(char in closed_delimiters):
        popped = Stack1.pop()
        if((char == ')' and popped == '(') or \
           (char == ']' and popped == '[' ) or \
           (char == '}' and popped == '{') ):
           pass 
        else:
          return False
  if(len(Stack1)==0):
    return True
  else:
    return False
        
        
    
    
  
  
  close(filename)
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')

