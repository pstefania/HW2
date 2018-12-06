import time
import random

def quickSort(alist,first,last):
    if first<last:
       splitpoint = partition(alist,first,last)
       quickSort(alist,first,splitpoint-1)
       quickSort(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark

alist = []
for x in range(100):
    alist.append (random.randint(1,10))
s = time.time()
quickSort(alist, 0, len(alist)-1)
e = time.time()
time1 = e-s








import time
import random

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


alist = []
for x in range(10):
    alist.append (random.randint(1,10))
s = time.time()
mergeSort(alist)
e = time.time()
time1 = e-s





import time
from mergesort import mergeSort
from quicksort import quickSort
import random

difference = []
for i in range (1,1000):
    alist = []
    for x in range(1000):
        alist.append (random.randint(1,1000))
    s = time.time()
    quickSort(alist, 0, len(alist)-1)
    e = time.time()
    time1 = e-s
    s = time.time()
    mergeSort(alist)
    e = time.time()
    time2 = e-s
    difference.append(time2-time1)
    print(i, 'quicksort:',time1,'mergesort;',time2,)
print ('the avarage difference in running time is:',sum(difference)/len(difference))

