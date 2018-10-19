import time
import random

def insertion_sort(arr):
  for k in range(1, len(arr)):
    item_to_place = arr[k]
    j = k
    while j > 0 and arr[j-1] > item_to_place:
      arr[j] = arr[j-1]
      j = j-1
    arr[j] = item_to_place

def selection_sort(arr):
    for k in range(0,len(arr)):
        smallestValue= arr[k]
        smallestI = k
        j = k + 1
        while j < len(arr):
            if smallestValue > arr[j]:
                smallestValue = arr[j]
                smallestI = j
            j += 1
        temp = arr[k]
        arr[k] = arr[smallestI]
        arr[smallestI] = temp 
if __name__ == '__main__':
  
#------------------------

    Increasing1 = []
    for i in range (0,1000):
        Increasing1.append(i)  
    Increasing2 = Increasing1

    Increasing3 = []
    for i in range (0,2500):
        Increasing3.append(i)
    Increasing4 = Increasing3
    
    Increasing5 = []
    for i in range (0,5000):
        Increasing5.append(i)
    Increasing6 = Increasing5
    
    Increasing7 = []
    for i in range (0,7500):
        Increasing7.append(i)
    Increasing8 = Increasing7
    
    Increasing9 = []
    for i in range (0,10000):
        Increasing9.append(i)
    Increasing10 = Increasing9
    
    #------------------------
    
    Decreasing1 = []
    for i in range (0,1000):
        Decreasing1.insert(0, i)  
    Decreasing2 = Decreasing1
    
    Decreasing3 = []
    for i in range (0,2500):
        Decreasing3.insert(0, i)
    Decreasing4 = Decreasing3
    
    Decreasing5 = []
    for i in range (0,5000):
        Decreasing5.insert(0, i)
    Decreasing6 = Decreasing5
    
    Decreasing7 = []
    for i in range (0,7500):
        Decreasing7.insert(0, i)
    Decreasing8 = Decreasing7
    
    Decreasing9 = []
    for i in range (0,10000):
        Decreasing9.insert(0, i)
    Decreasing10 = Decreasing9
    
    #------------------------
    
    Random1 = []
    for i in range (0,1000):
        Random1.append(random.randint(0, 1000))
    Random2 = Random1
    
    Random3 = []
    for i in range (0,2500):
        Random3.append(random.randint(0, 2500))
    Random4 = Random3
    
    Random5 = []
    for i in range (0,5000):
        Random5.append(random.randint(0, 5000))
    Random6 = Random5
    
    Random7 = []
    for i in range (0,7500):
        Random7.append(random.randint(0, 7500))
    Random8 = Random7
    
    Random9 = []
    for i in range (0,10000):
        Random9.append(random.randint(0, 10000))
    Random10 = Random9
    
    #------------------------
    insert=open('insert.txt','w')
    select=open('selection.txt','w')
    start = time.clock()
    insertion_sort(Increasing1)
    end = time.clock() 
    print('1000 Increasing1 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    
    start = time.clock()
    selection_sort(Increasing2)
    end= time.clock()
    print('1000 Increasing2 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    insertion_sort(Increasing3)
    end = time.clock() 
    print('2500 Increasing3 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Increasing4)
    end= time.clock()
    print('2500 Increasing4 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))

    start = time.clock()
    insertion_sort(Increasing5)
    end = time.clock() 
    print('5000 Increasing5 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Increasing6)
    end= time.clock()
    print('5000 Increasing6 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))

    start = time.clock()
    insertion_sort(Increasing7)
    end = time.clock() 
    print('7500 Increasing7 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Increasing8)
    end= time.clock()
    print('7500 Increasing8 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))

    start = time.clock()
    insertion_sort(Increasing9)
    end = time.clock() 
    print('10000 Increasing9 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Increasing10)
    end= time.clock()
    print('10000 Increasing10 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))

    #------------------------
    
    start = time.clock()
    insertion_sort(Decreasing1)
    end = time.clock() 
    print('1000 Decreasing1 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Decreasing2)
    end = time.clock() 
    print('1000 Decreasing2 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    insertion_sort(Decreasing3)
    end = time.clock() 
    print('2500 Decreasing3 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Decreasing4)
    end = time.clock() 
    print('2500 Decreasing4 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    insertion_sort(Decreasing5)
    end = time.clock() 
    print('5000 Decreasing5 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Decreasing6)
    end = time.clock() 
    print('5000 Decreasing6 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    insertion_sort(Decreasing7)
    end = time.clock() 
    print('7500 Decreasing7 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Decreasing8)
    end = time.clock() 
    print('7500 Decreasing8 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    insertion_sort(Decreasing9)
    end = time.clock() 
    print('10000 Decreasing9 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Decreasing10)
    end = time.clock() 
    print('10000 Decreasing10 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))
    
    #------------------------
    
    start = time.clock()
    insertion_sort(Random1)
    end = time.clock() 
    print('1000 Random1 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Random2)
    end = time.clock() 
    print('1000 Random2 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    insertion_sort(Random3)
    end = time.clock() 
    print('2500 Random3 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Random4)
    end = time.clock() 
    print('2500 Random4 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    insertion_sort(Random5)
    end = time.clock() 
    print('5000 Random5 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Random6)
    end = time.clock() 
    print('5000 Random6 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    insertion_sort(Random7)
    end = time.clock() 
    print('7500 Random7 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Random8)
    end = time.clock() 
    print('7500 Random8 Selection: ' + '{:.20f}'.format(end-start) + '\n')
    select.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    insertion_sort(Random9)
    end = time.clock() 
    print('10000 Random9 Insertion: ' + '{:.20f}'.format(end-start))
    insert.write('{:.20f}\n'.format(end-start))
    
    start = time.clock()
    selection_sort(Random10)
    end = time.clock() 
    print('10000 Random10 Selection: ' + '{:.20f}'.format(end-start))
    select.write('{:.20f}\n'.format(end-start))
    select.close()
    insert.close()