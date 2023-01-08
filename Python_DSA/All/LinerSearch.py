# Program to inpliment Linear Search:

# Time Complexity of QuickSort:         |   Space Complexity   
#       BEST        AVERAGE     WORST   |   WORST
#       O(1)        O(n)        O(n)   |   log(n)    


def search(arr, x):
 
    for i in range(len(arr)):
        if arr[i] == x:
            return i
 
    return -1

arr = [1,4,7,8,9,3,4,5,6,7]
target = 5
print(search(arr,5))


# Searching an element in a list/array in python
# can be simply done using \'in\' operator
# Example:
# if x in arr:
#   print arr.index(x)
 
# If you want to implement Linear Search in python
 
# Linearly search x in arr[]
# If x is present then return its location
# else return -1
 
def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1