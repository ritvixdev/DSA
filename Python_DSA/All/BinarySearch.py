# Program to impliment Binary Search:

# Time Complexity of BinarySearch:       |   Space Complexity   
#       BEST        AVERAGE     WORST    |   WORST
#       O(1)        O(log n)   O(log n)  |   O(1)   

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return -1
 

arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
result = binary_search(arr, x)
print(result)




# Program Explained:

# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")