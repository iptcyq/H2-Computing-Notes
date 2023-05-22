size = int(input("Enter size of array between 5 and 12: "))
while size<5 and size>12:
    size = int(input("Enter size of array BETWEEN 5 and 12: "))

arr = []
for i in range(size):
    inp = input("Enter an integer number: ")
    arr.append(int(inp))


def sort(arr):
    if len(arr)==0:
        return []
    mid = arr.pop(0)
    left = []
    right = []
    while len(arr)>0:
        val = arr.pop()
        left.append(val) if val<mid else right.append(val)
    return sort(left)+[mid]+sort(right)

arr = sort(arr)
for i in arr:
    print(i, end=" ")
