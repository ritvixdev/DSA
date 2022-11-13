# Linear Search in Python


# def linearSearch(array, n, x):

#     # Going through array sequencially
#     for i in range(0, n):
#         if (array[i] == x):
#             return i
#     return -1


# array = [2, 4, 0, 1, 9]
# x = 1
# n = len(array)
# result = linearSearch(array, n, x)
# if(result == -1):
#     print("Element not found")
# else:
#     print("Element found at index: ", result)



#search the target and return treue or false

def linearSearch(arr, target):
    if len(arr) == 0:
        return False
    
    #run for a 
    for element in arr:
        if element == target:
            return True

    return False

nums = [23, 45,1,2,8,29,-3,26,-11,28]
target = 23
ans  = linearSearch(nums, target)
print(ans)



# def LinearSearch(array, n, k):

#     for j in range(0, n):

#         if (array[j] == k):

#             return j

#     return -1

 
# array = [1, 3, 5, 7, 9]

# k = 7
# n = len(array)

# result = LinearSearch(array, n, k)

# if(result == -1):

#     print("Element not found")

# else:

#     print("Element found at index: ", result)

# def linearSearch(data, target):
#     for i in range(len(data)):
#         if data[i] == item:
            
#             return i
#         return -1


# data = [1, 9, 8, 7, 6, 3, 11, 4, 6, 9, 7, 2, 0, 19, -10]
# target = 4
# idx = linearSearch(data, target)
# if idx >= 0:
#     print("{} is found at index {}".format(target, idx))
# else :
#     print("{} was not found".format(target)))