# Binary Search on sorted 2D Array

def findAns(lst, target):
    row = 0
    col = len(lst[row]) - 1
    while (row < len(lst) and col >= 0):
        if (lst[row][col] == target):
            return [row, col]
 
        # Target lies in further row
        if (lst[row][col] < target):
            row += 1
 
        # Target lies in previous column
        else:
            col -= 1
 
    return [-1, -1]
 
 
# Driver Code
if __name__ == '__main__':
    # Binary search in sorted matrix
    lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ans = findAns(lst, 12)
    print("Element found at index: ", ans)