# Insertion sort
# In place/ most common sort

import Utils

def InsertionSort(arr):
    if len(arr) <= 1: # edge case
        return arr

    for i in range(1,len(arr)): # for every item
        curr = i # current swapping index
        while curr > 0 and arr[curr-1] > arr[curr]: # wrong pos
            arr[curr], arr[curr-1] = arr[curr-1], arr[curr] # swap backwards
            curr -= 1

    return arr

nums = Utils.CreateRandomList()
print("Before sorted:", nums, "\n")
InsertionSort(nums)
print("After sorted:", nums, "\n")
check = Utils.CheckSorted(nums)
print(check)
