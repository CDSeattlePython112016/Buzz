import random

rand = []

for i in range(101):
    i = random.random() * 10000   
    i = int(round(i) -1)
    rand.append(i)


def bubbleSort(rand):
    for i in range(len(rand)-1, 0, -1):
        for x in range(i):
            if (rand[x] > rand[x+1]):
                temp = rand[x]
                rand[x] = rand[x+1]
                rand[x+1] = temp
    return rand
                
print(rand)
print(bubbleSort(rand))
      
