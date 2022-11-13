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
