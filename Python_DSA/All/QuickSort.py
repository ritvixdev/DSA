# Python program for implementation of Quicksort Sort

# Time Complexity of QuickSort:         |   Space Complexity   
#       BEST        AVERAGE     WORST   |   WORST
#       nlog(n)     nlog(n)     (n^2)   |   log(n)    

# GeekOfGeeks Method:
def partition(array, low, high):

    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1
 
 
def quickSort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
 
 
data = [1, 7, 4, 1, 10, 9, -2]
size = len(data)
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)


# Program explained:

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot
 
 
# Function to find the partition position
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
 
 
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)


# chatGPT Method:

def quick_sort(list):
    if len(list) <= 1:
        return list

    pivot = list[0]
    left = []
    right = []

    for i in range(1, len(list)):
        if list[i] < pivot:
            left.append(list[i])
        else:
            right.append(list[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

data = [1, 7, 4, 1, 10, 9, -2]
size = len(data)
sorted_list = quick_sort(data)
 
print('Sorted Array in Ascending Order:')
print(sorted_list)

