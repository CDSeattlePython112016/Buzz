import random

rand = []



for i in range(101):
    i = random.random() * 10000   
    i = int(round(i) -1)
    rand.append(i)
    

def SelectionSort(rand):
    
    for i in range ( len(rand)):
        least = i
        
        for y in range(i+1, len(rand)):
            if(rand[y] < rand[least]):
                least = y
        
        swap( rand, least, i)           
      
    return rand


def swap(A,k,l):
    tmp = A[k]
    A[k] = A[l]
    A[l] = tmp
print(rand)
print(SelectionSort(rand))



 
