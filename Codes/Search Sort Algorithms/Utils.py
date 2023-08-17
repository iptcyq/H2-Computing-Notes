# Utility script for sort/ search algos

from random import randint

def CreateRandomList(size=51, minm=1, maxm=500):
    nums = []
    for i in range(size):
        nums.append(randint(minm,maxm))
    return nums

def CheckSorted(l): # check if nums is sorted 
    check = True
    for i in range(1, len(l)):
        if l[i-1] > l[i]: # if not in order
            check = False # uncheck
    return check
