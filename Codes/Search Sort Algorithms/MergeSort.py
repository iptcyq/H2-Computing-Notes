# Merge Sort
# Basic/ easiest to do : ifk if there are other methods

import Utils

def MergeSort(arr):
    if len(arr) > 1: # base case
        mid = len(arr)//2
        left = MergeSort(arr[:mid]) # sort left half
        right = MergeSort(arr[mid:]) # sort right half
        arr = []
        while len(left)>0 and len(right)>0:
            if left[0] > right[0]: # append right if less
                arr.append(right.pop(0))
            else: # otherwise left
                arr.append(left.pop(0))
        arr = arr + left + right
    return arr

nums = Utils.CreateRandomList()
print("Before sorted:", nums, "\n")
sortd = MergeSort(nums)
print("After sorted:", sortd, "\n")
check = Utils.CheckSorted(sortd)
print(check)
