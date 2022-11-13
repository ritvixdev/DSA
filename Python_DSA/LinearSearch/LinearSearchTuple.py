def linearSearch(tuple, target):
 
    for i in range(len(tuple)):
        if tuple[i] == target:
            return i
    return -1
 
 
# tuple which contains both string and numbers.
tuple = ('apple', 9, 'blueberry', 4, 'avocardo', 6)
 
# Driver Code
target = 4
ans = linearSearch(tuple, target)
 
if ans >= 0:
    print(f"{target} is found at index {ans}")
else :
    print(f"{target} was not found")