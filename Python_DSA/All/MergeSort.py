# Python program for implementation of MergeSort

# Time Complexity of MergeSort:         |   Space Complexity   
#       BEST        AVERAGE     WORST   |   WORST
#       nlog(n)     nlog(n)     nlog(n) |   O(n)    


def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:]      
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

  
arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print("Sorted array is: ", end="\n")
printList(arr)



# Program Explained:

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
# Code to print the list
 
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    
    
# Properties:

# Worst case complexity:    O(nlogn)
# Works well on:            It operates fine on any size of array
# Speed of execution:       It has a consistent speed on any size of data
# Efficiency:               More efficient
# Sorting method:           External
# Stability:                Stable
# Preferred for:            Linked Lists
# Locality of reference:    poor
