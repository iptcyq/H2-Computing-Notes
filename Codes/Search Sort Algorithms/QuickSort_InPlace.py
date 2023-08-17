# Quick sort
# In place : (No usage of new arrays)

import Utils

# sort
def QuickSort(arr, left, right): # add defaults to left right if needed
    if left >= right: # base case
        return arr

    ptr = left+1 # separator of larger and smaller 
    for i in range(left+1, right):
        if arr[i] < arr[left]: # move to right of separator
            arr[i], arr[ptr] = arr[ptr], arr[i] # swap pos
            ptr += 1 # separator shifts an index
    arr[left], arr[ptr-1] = arr[ptr-1], arr[left] # swap separator and mid

    QuickSort(arr, left, ptr-1) # sort the left
    QuickSort(arr, ptr, right) # sort the right
    return arr

nums = Utils.CreateRandomList()
print("Before sorted:", nums, "\n")
QuickSort(nums, 0, 51)
print("After sorted:", nums, "\n")
check = Utils.CheckSorted(nums)
print(check)
