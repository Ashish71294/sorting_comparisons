import random
count =0
 
def quicksort( aList ):
    _quicksort( aList, 0, len( aList ) - 1 )
 
def _quicksort( aList, first, last ):
    if first < last:
      pivot = partition( aList, first, last )
      _quicksort( aList, first, pivot - 1 )
      _quicksort( aList, pivot + 1, last )
 
 
def partition( aList, first, last ) :
    global count
    pivot = first + random.randrange( last - first + 1 )
    swap( aList, pivot, last )
    for i in range( first, last ):
      if aList[i] <= aList[last]:
        count =count +1
        swap( aList, i, first )
        first += 1
      else:
        count = count +1
    swap( aList, first, last )
    return first
 

def swap( A, x, y ):
  A[x],A[y]=A[y],A[x]


for i in range(10):
    alist = random.sample(xrange(100),20)
    print(alist)
    quicksort(alist)
    print(alist)
    print(count)
print(count/10)  