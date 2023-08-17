# Quick sort
# Typical/ easiest : (out of place)

import Utils

def QuickSort(arr):
    if len(arr) > 1: # base case
        left = []
        right = []
        for i in arr[1:]:
            if i> arr[0]: # right list
                right.append(i)
            else: # left list
                left.append(i)
        arr = MergeSort(left) + [arr[0]] + QuickSort(right) # recursive
    return arr

nums = Utils.CreateRandomList()
print("Before sorted:", nums, "\n")
sortd = QuickSort(nums)
print("After sorted:", sortd, "\n")
check = Utils.CheckSorted(sortd)
print(check)
