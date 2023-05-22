# bubble sort
def bubble_sort(arr):
    print(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j+1<len(arr) and arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)
    return arr

# insertion sort
def insertion_sort(arr):
    print(arr)
    unsorted = True
    for i in range(len(arr)):
        for j in range(len(arr)):
            while j+1<len(arr) and arr[j] > arr[j+1]:
                unsorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
            if unsorted:
                break
    print(arr)
    return arr

#incomplete - need check if i mixed them up
a = [432,7,452,37,8,345,85,36]
print(bubble_sort(a))

a = [432,7,452,37,8,345,85,36]
print(insertion_sort(a))
