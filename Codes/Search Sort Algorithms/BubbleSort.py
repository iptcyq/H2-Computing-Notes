# Bubble sort
# Easiest : (Not efficient)

import Utils

def BubbleSort(arr):
    for i in range(len(arr)): # for every item
        for j in range(len(arr)-i-1): # for every item except prev last
            if arr[j] > arr[j+1]: # if not sorted
                arr[j], arr[j+1] = arr[j+1], arr[j] # sort
    return arr

nums = Utils.CreateRandomList()
print("Before sorted:", nums, "\n")
BubbleSort(nums)
print("After sorted:", nums, "\n")
check = Utils.CheckSorted(nums)
print(check)
