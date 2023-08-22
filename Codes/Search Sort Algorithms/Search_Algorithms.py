# linear search
def linear_search(arr, target):
	for i in range(len(arr)):
		if target == arr[i]:
			return True
	return False

#binary search
def binary_search_rec(arr, target):
	if len(arr) == 0:
		return False
	mid = arr[len(arr)//2]
	if target < mid:
		return binary_search_rec(arr[:mid], target)
	elif target > mid:
		return binary_search_rec(arr[mid+1:],target)
	else:
		return True

def binary_search(arr, target):
	mid = len(arr)//2
	top = len(arr)-1
	bottom = 0
	while bottom < top:
                if target < arr[mid]:
			top =  mid
			mid = (top + bottom)//2
		elif target > arr[mid]:
			bottom = mid + 1
			mid = (top + bottom)//2
		else:
			return True
	return False

# hash table search
# nah hash table search is ez claps
