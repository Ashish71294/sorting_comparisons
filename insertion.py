import random
count = 0

def insertionSort(alist):
	global count
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index
		while position>0 and alist[position-1]>currentvalue:
			alist[position]=alist[position-1]
			position = position - 1
			count =count + 1
		alist[position]=currentvalue
alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)


for i in range(10):
    alist = random.sample(xrange(100),10)
    print(alist)
    insertionSort(alist)
    print(alist)
    print(count)
print(count/10) 