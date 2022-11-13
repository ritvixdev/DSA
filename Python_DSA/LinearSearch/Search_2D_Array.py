# Linear Search in 2D Arrays

def linearSearch (lst, target):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if (lst[i][j] == target):
                return [i, j]
    return [-1, -1]
 
# Driver code
lst = [[3, 12, 9], [5, 2, 89], [90, 45, 22]]
target = 89
ans = linearSearch(lst, target)
print(f"Element found at index: [{ans[0]} {ans[1]}]")