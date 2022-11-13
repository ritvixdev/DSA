# Code for linear search

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [1, 9, 8, 7, 6, 3, 11, 4, 6, 9, 7, 2, 0, 19, -10]
target = -10
ans = linearSearch(arr, target)
if ans >= 0:
    print(f"{target} is found at index {ans}")
else :
    print(f"{target} was not found")
