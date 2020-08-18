from array import *




def quickSort(array1,start,end):
    if(start>= end):
        return

    partIndex = doPartition(array1, start, end)
    quickSort(array1,start,partIndex-1)
    quickSort(array1,partIndex+1,end)

def doPartition(a, start, end):
    pivot = a[end]
    pIndex = start-1
    for i in range(start,end):
        if pivot > a[i]:
            pIndex = pIndex+1
            a[pIndex],a[i] = a[i],a[pIndex]

    a[pIndex+1],a[end] = a[end],a[pIndex+1]
    print(pIndex+1)
    print(a)
    return pIndex+1



array1 = array('i', [13,19,9,5,12,8,7,4,21,2,6,11])
quickSort(array1,0,len(array1)-1);

for x in array1:
    print(x)








