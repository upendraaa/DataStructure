from array import *

def hoare_quick_sort(arr, low ,high):
    pivot = arr[low]
    i = low -1
    j = high +1

    while True:

        j = j-1
        while arr[j] > pivot:
            j = j-1

        i = i+1
        while arr[i]< pivot:
            i= i+1

        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            return j


def recursive_quick_sort(arr,low, high):
    while low<high:
        print(arr)
        index = hoare_quick_sort(arr,low,high)
        recursive_quick_sort(arr,low,high-1)
        low = high+1


array = array('i',[2,5,34,65,21,6,7])
recursive_quick_sort(array,0,len(array)-1)
