# in place quick sort with no new arrays

from random import randint

# list of integers
nums = []
for i in range(51):
    nums.append(randint(1,500))

print("Before sorted: ")
print(nums)
print()

# sort
def quick(arr, left=0, right=None):
    if right == None: # start case
        right = len(arr)
    elif left >= right: # base case
        return arr

    ptr = left+1 # mid  
    for i in range(left+1, right):
        if arr[i] < arr[left]: # move to right
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    arr[left], arr[ptr-1] = arr[ptr-1], arr[left]

    quick(arr, left, ptr-1)
    quick(arr, ptr, right)
    return arr

print("After sorted: ")
quick(nums)
print(nums)
print()

# check sorted
check = True
for i in range(1, len(nums)):
    if nums[i-1] > nums[i]:
        check = False
print("Check:", check)
