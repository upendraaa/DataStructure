
import random
from array import *


def randomize_partition(arr,low,high):
    random_index = random.randint(low,high)
    arr[random_index],arr[high] = arr[high],arr[random_index]
    return partition(arr,low,high)



def partition(arr,low,high):
    pivot = arr[high]
    index = low -1;

    for j in range(low,high):
        if arr[j] < pivot:
            index = index+1
            arr[index],arr[j] = arr[j],arr[index]
    arr[index+1],arr[high] = arr[high],arr[index+1]
    print(index+1)
    print(arr)
    return (index+1)

def randomize_quick_sort(arr,low,high):
    if(low>=high):
        return
    pivot_index = randomize_partition(arr,low,high)
    randomize_quick_sort(arr,low,pivot_index-1)
    randomize_quick_sort(arr,pivot_index+1,high)

arr = array('i', [13,19,9,5,12,8,7,4,21,2,6,11])
randomize_quick_sort(arr,0,len(arr)-1)

print(arr)