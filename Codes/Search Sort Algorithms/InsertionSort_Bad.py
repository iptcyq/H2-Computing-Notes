# Insertion sort
# Bad : (creates a whole new list)

import Utils

def InsertionSort(arr): # not a mutable function
    sortd = [] # new list
    for i in arr:
        pos = 0
        while pos<len(sortd) and i > sortd[pos]: # find correct pos
            pos += 1
        sortd = sortd[:pos] + [i] + sortd[pos:] # put at sorted
    return sortd

nums = Utils.CreateRandomList()
print("Before sorted:", nums, "\n")
nums = InsertionSort(nums)
print("After sorted:", nums, "\n")
check = Utils.CheckSorted(nums)
print(check)
