import random   
count = 0
def mergeSort(alist):
    #print("Splitting ",alist)
    global count
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
                count =count + 1
            else:
                alist[k]=righthalf[j]
                j=j+1
                count =count + 1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

for i in range(10):
    alist = random.sample(xrange(3000),10)
    print(alist)
    mergeSort(alist)
    print(alist)
    print(count)
print(count/10)    
