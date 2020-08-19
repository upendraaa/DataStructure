from array import *

def hoare_partition(arr,start,end):
    x = arr[start]
    i = start-1
    j = end+1
    while (True):
        j = j-1
        while arr[j] > x:
            j = j-1

        i = i+1
        while arr[i] < x:
            i = i+1

        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            return j


def quick_sort(arr,start,end):
    if(end<=start):
        return

    pivot = hoare_partition(arr,start,end)
    quick_sort(arr,start,pivot)
    quick_sort(arr,pivot+1,end)


arr = array('i', [13,19,9,5,12,8,7,4,21,2,6,11])
quick_sort(arr,0,len(arr)-1)
print(arr)