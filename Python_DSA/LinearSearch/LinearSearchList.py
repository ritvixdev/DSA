
def linearSearch(list, target):
    
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
 
 
# list which contains both string and numbers.
list = ['apple', 9, 'blueberry', 4, 'avocardo', 6]
 
# Driver Code
target = 'avocardo'
ans = linearSearch(list, target)
 
if ans >= 0:
    print(f"{target} is found at index {ans}")
else :
    print(f"{target} was not found")